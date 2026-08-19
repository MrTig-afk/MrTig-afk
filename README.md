<picture>
  <source media="(prefers-color-scheme: dark)" srcset="header-dark.svg">
  <img alt="Kaushik N, backend engineer, Melbourne. 5 pull requests merged upstream, 1,651 tests." src="header-light.svg" width="880">
</picture>

[![Portfolio](https://img.shields.io/badge/Portfolio-0E6E7D?style=flat-square)](https://portfolio-mrtig-afks-projects.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square)](https://www.linkedin.com/in/kaushikn2002/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square)](mailto:kaushiknaru2002@gmail.com)
[![Medium](https://img.shields.io/badge/Medium-1F2937?style=flat-square)](https://medium.com/@kaushiknaru2002)

**OPEN SOURCE CONTRIBUTOR**

[![Reactive Resume](https://img.shields.io/badge/AmruthPillai%2FReactive--Resume-0F172A?style=flat-square)](https://github.com/AmruthPillai/Reactive-Resume/pulls?q=is%3Apr+author%3AMrTig-afk)
[![qm](https://img.shields.io/badge/yc--software%2Fqm-0F172A?style=flat-square)](https://github.com/yc-software/qm/pulls?q=is%3Apr+author%3AMrTig-afk)
[![whatsapp-claude-plugin](https://img.shields.io/badge/Rich627%2Fwhatsapp--claude--plugin-0F172A?style=flat-square)](https://github.com/Rich627/whatsapp-claude-plugin/pulls?q=is%3Apr+author%3AMrTig-afk)
[![crap](https://img.shields.io/badge/thomasdavis%2Fcrap-0F172A?style=flat-square)](https://github.com/thomasdavis/crap/pulls?q=is%3Apr+author%3AMrTig-afk)

---

## Experience

### Backend Engineering Intern &nbsp;·&nbsp; Skilliphy &nbsp;·&nbsp; Jul 2025 to Jan 2026

**AI Skill Recommender**

`free-text résumé` → `deterministic parse` → `embedding search` → `ranked skill graph`

Dual inference path: rule-based parsing for precision, embedding search for recall, selectable per request. Log-scaled evidence weighting with recruiter outcomes feeding back into ranking.

<sub>FastAPI · Sentence-Transformers · AWS Cognito</sub>

---

## Selected Work

### 01 &nbsp;·&nbsp; MingleHub &nbsp;·&nbsp; [Live demo](https://mingle-hub.vercel.app/fifty-five-bar/1) &nbsp;·&nbsp; [Code](https://github.com/MrTig-afk/MingleHub)

`NFC tap` → `FastAPI / Mangum` → `session + billing` → `Postgres · Stripe`

459 tests. Venue is derived from the auth token, never the request, so cross-tenant reads are impossible by construction. Billing is idempotent, so re-running invoicing cannot double-charge.

<sub>FastAPI · Postgres · Stripe · Supabase Realtime</sub>

### 02 &nbsp;·&nbsp; Finance Tracker &nbsp;·&nbsp; [Code](https://github.com/MrTig-afk/FinanceTracker)

`bank CSV` → `detect source` → `fingerprint + dedupe` → `Postgres`

1,192 tests. Every row is fingerprinted, so re-uploading an unchanged statement is a no-op. Raw statements never leave the machine.

<sub>Python · Postgres · PWA</sub>

### 03 &nbsp;·&nbsp; NutriScan &nbsp;·&nbsp; [Live](https://nutritional-tracker-delta.vercel.app/) &nbsp;·&nbsp; [Code](https://github.com/MrTig-afk/NutritionalTracker)

`label photo` → `Gemini → fallback` → `validate` → `Postgres RLS`

Isolation enforced by Postgres row-level security rather than by application code remembering to filter. ES256 JWTs verified server-side via JWKS.

<sub>FastAPI · Neon · Gemini · Groq</sub>

### 04 &nbsp;·&nbsp; LinkedIn Formatter &nbsp;·&nbsp; [Marketplace](https://marketplace.visualstudio.com/items?itemName=kaushiknaru.linkedin-formatter) &nbsp;·&nbsp; [npm](https://www.npmjs.com/package/linkedin-fmt) &nbsp;·&nbsp; [MCP](https://www.npmjs.com/package/linkedin-formatter-mcp) &nbsp;·&nbsp; [Code](https://github.com/MrTig-afk/linkedin-formatter)

`.linkedin file` → `formatting core` → `VS Code · CLI · MCP`

One core shipped as three published artifacts across two registries. The MCP server speaks stdio, so an agent calls the same code the editor does.

<sub>TypeScript · Model Context Protocol · npm</sub>

---

**Architecture write-ups, dashboards and walkthroughs → [portfolio-mrtig-afks-projects.vercel.app](https://portfolio-mrtig-afks-projects.vercel.app)**
