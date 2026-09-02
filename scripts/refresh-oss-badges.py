#!/usr/bin/env python3
"""Regenerate the Open source badge row in README.md from GitHub.

Every repo Kaushik has a MERGED pull request in gets two badges: a live star
count, and a live merged-PR count (a shields.io dynamic/json badge reading
$.total_count from the GitHub search API, so it updates itself on the next
merge without anyone touching this repo).

Repos in NO_MERGE_YET are listed with a star badge only. They are open
contributions or accepted work that never became a PR of ours, so a merged
count would read 0 and say the wrong thing.

Usage:
    python scripts/refresh-oss-badges.py --dry-run   # print, change nothing
    python scripts/refresh-oss-badges.py             # rewrite README.md
    python scripts/refresh-oss-badges.py --self-test # offline sanity check

Needs `gh` on PATH and authenticated. Never pushes; commit and push by hand.
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.parse

USER = "MrTig-afk"
START = "<!-- oss:start -->"
END = "<!-- oss:end -->"

# Repos worth showing that have no merged PR of ours. Value is the link target.
# thomasdavis/crap was dropped 2026-09-02: a real PR of ours, but unmerged, in
# a 4-star repo whose last commit predates it. The badge earned nothing.
NO_MERGE_YET = {
    "yc-software/qm": "https://github.com/yc-software/qm/pulls?q=is%3Apr+author%3A" + USER,
}

# Repos to keep out of the row entirely (own repos are filtered automatically).
# ai-skill-recommender is Skilliphy internship work, not an open source
# contribution; it belongs under Experience and must never inflate this row.
SKIP = {"DhaneshRamesh/ai-skill-recommender"}

# Merged badge but no star badge: a real merged PR in a repo whose star count
# would undersell it. The merge is the claim; the stars are not.
NO_STAR_BADGE = set()

COLOR = "color=0E6E7D&labelColor=0F172A"


def sh(*args):
    out = subprocess.run(args, capture_output=True, text=True)
    if out.returncode:
        sys.exit("command failed: %s\n%s" % (" ".join(args), out.stderr.strip()))
    return out.stdout


def canonical(repo):
    """GitHub search lowercases owner/name; badges must show the real casing."""
    return sh("gh", "repo", "view", repo, "--json", "nameWithOwner",
              "--jq", ".nameWithOwner").strip()


def merged_by_repo():
    """{repo: count} for every repo with a merged PR by USER, excluding own."""
    raw = sh("gh", "search", "prs", "--author", USER, "--merged",
             "--limit", "200", "--json", "repository")
    counts = {}
    for row in json.loads(raw):
        repo = row["repository"]["nameWithOwner"]
        if repo.lower().startswith(USER.lower() + "/"):
            continue
        if repo in SKIP:
            continue
        counts[repo] = counts.get(repo, 0) + 1
    return {canonical(r): n for r, n in counts.items()}


def star_badge(repo, link):
    label = urllib.parse.quote(repo, safe="")
    return ("[![%s](https://img.shields.io/github/stars/%s?style=flat-square"
            "&label=%s&%s)](%s)" % (repo, repo, label, COLOR, link))


def merged_badge(repo):
    api = ("https://api.github.com/search/issues?q=repo:%s+author:%s"
           "+is:pr+is:merged" % (repo, USER))
    link = ("https://github.com/%s/pulls?q=is%%3Apr+author%%3A%s+is%%3Amerged"
            % (repo, USER))
    return ("[![merged](https://img.shields.io/badge/dynamic/json?url=%s"
            "&query=%%24.total_count&label=merged&%s&style=flat-square)](%s)"
            % (urllib.parse.quote(api, safe=""), COLOR, link))


def build_block(counts, no_star=None):
    lines = []
    # Most merges first, so the strongest relationship leads the row.
    for repo in sorted(counts, key=lambda r: (-counts[r], r)):
        link = ("https://github.com/%s/pulls?q=is%%3Apr+author%%3A%s"
                % (repo, USER))
        if repo not in (NO_STAR_BADGE if no_star is None else no_star):
            lines.append(star_badge(repo, link))
        lines.append(merged_badge(repo))
    for repo, link in NO_MERGE_YET.items():
        lines.append(star_badge(repo, link))
    return "\n".join(lines)


def self_test():
    counts = {"a/one": 10, "b/two": 3}
    block = build_block(counts)
    assert block.index("a/one") < block.index("b/two"), "not sorted by merges"
    assert block.count("dynamic/json") == 2, "one merged badge per merged repo"
    starless = build_block({"x/paid-work": 1}, no_star={"x/paid-work"})
    own = [l for l in starless.splitlines() if "paid-work" in l]
    assert len(own) == 1, "a NO_STAR_BADGE repo should emit exactly one badge"
    assert "dynamic/json" in own[0], "NO_STAR_BADGE repo lost its merged badge"
    assert "github/stars" not in own[0], "NO_STAR_BADGE repo still got a star badge"
    for repo in NO_MERGE_YET:
        rows = [l for l in block.splitlines() if repo in l]
        assert len(rows) == 1, "expected 1 badge for %s, got %d" % (repo, len(rows))
        assert "github/stars" in rows[0], "%s lost its star badge" % repo
        assert "dynamic/json" not in rows[0], (
            "%s has no merged PR and must not get a merged badge" % repo)
    for gone in ("thomasdavis/crap", "jsonresume", "ai-skill-recommender"):
        assert gone not in block, "%s must stay out of the row" % gone
    assert "%24.total_count" in block, "query param must stay url-encoded"
    print("self-test ok")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    counts = merged_by_repo()
    if not counts:
        sys.exit("no merged PRs found; refusing to write an empty row")
    block = build_block(counts)
    total = sum(counts.values())
    print("%d merged PRs across %d projects: %s"
          % (total, len(counts),
             ", ".join("%s (%d)" % (r, n) for r, n in sorted(counts.items()))))

    readme = open("README.md", encoding="utf-8").read()
    if START not in readme or END not in readme:
        sys.exit("markers %s / %s not found in README.md" % (START, END))

    new = re.sub(re.escape(START) + r".*?" + re.escape(END),
                 START + "\n" + block + "\n" + END, readme, flags=re.S)

    if args.dry_run:
        print("\n" + block)
        print("\n(dry run, README.md unchanged)")
        return
    if new == readme:
        print("README.md already current")
        return
    open("README.md", "w", encoding="utf-8", newline="").write(new)
    print("README.md updated. Review, commit and push by hand.")


if __name__ == "__main__":
    main()
