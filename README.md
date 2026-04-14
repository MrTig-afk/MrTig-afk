# Hi there, I'm Kaushik! 👋

## 🚀 Data Engineer & AI Systems Builder

I build end-to-end data systems that transform **raw, unstructured data into production-ready insights**.

My focus:
- Designing **scalable data pipelines**
- Leveraging **LLMs for real-world extraction & automation**
- Deploying **cloud-native, full-stack data products**

Currently based in **Melbourne, Australia** 🇦🇺

---

## 🛠️ Tech Stack

| Domain | Technologies |
| :--- | :--- |
| **Languages** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) |
| **Data & Storage** | ![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat&logo=duckdb&logoColor=black) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white) ![AWS S3](https://img.shields.io/badge/AWS_S3-569A31?style=flat&logo=amazonaws&logoColor=white) |
| **AI / ML** | ![Gemini](https://img.shields.io/badge/Gemini-4285F4?style=flat&logo=google&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white) |
| **Backend** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) ![REST API](https://img.shields.io/badge/REST-API-FF6F00?style=flat) |
| **Frontend** | ![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black) ![TailwindCSS](https://img.shields.io/badge/Tailwind-38B2AC?style=flat&logo=tailwindcss&logoColor=white) |
| **Cloud & Deployment** | ![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white) ![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=black) |
| **Tools** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) |

---

## 🔭 Featured Projects

### 🥗 NutriScan — Multimodal Nutrition Extraction Pipeline
🔗 https://nutritional-tracker-delta.vercel.app/

*A cloud-native data pipeline that converts nutrition label images into structured data using multimodal LLM inference.*

#### 🚀 Key Innovation

- **Multi-Image iPhone Support:** Handles multiple images (common from iPhone camera uploads) in a **single multimodal API request**
- **Optimized Image Pipeline:** Client + server-side compression, resizing, and preprocessing to reduce latency and token usage
- **Robust Inference Flow:** Retry + fallback handling for real-world API instability (503 / 429 scenarios)

#### ⚙️ Architecture

React (Frontend)
→ Image Optimization (Crop + Resize + Compress)
→ FastAPI Backend
→ AWS S3 (Raw + Processed Storage)
→ Gemini 2.5 Flash (Multimodal Inference)
→ DuckDB (Analytical Storage)

#### 📦 Core Features

- 📸 Upload multiple images directly from iPhone  
- ⚡ Process all images in a **single request**  
- 🧠 Extract structured nutrition data (JSON format)  
- 🔁 Resilient pipeline with retry + fallback handling  
- ☁️ Cloud-native architecture (S3 + Render + Vercel)  

#### 🧠 Engineering Focus

This project focuses on solving **real-world multimodal pipeline challenges**:

- Handling **large mobile image uploads**  
- Reducing **LLM token cost via preprocessing**  
- Designing **fault-tolerant inference pipelines**  
- Supporting **batch inputs without increasing API calls linearly**  

---

### 📄 AI Skill Recommender & Parsing Pipeline (Internship)

*High-volume hybrid inference system for deterministic and semantic skill mapping.*

**Tech Stack:** FastAPI, Python 3.13, Sentence-Transformers, AWS Cognito, SQLite, PDFPlumber  

**Architecture:** Dual-pipeline system combining:
- Deterministic parsing (structured extraction)
- Skill Graph + Hybrid Inference (semantic discovery)

**Engine Modes:**
- Deterministic (rule-based precision)  
- Hybrid (fusion)  
- AI-only (embedding-driven discovery)  

**Mathematical Core:**
- Log-scaled evidence weighting  
- Confidence calibration  
- Feedback-driven ranking optimization  

**Impact:**
- Drift monitoring  
- Offline evaluation (Precision / Recall / F1)  
- Recruiter outcome-based learning loops  

**Focus:**
Production-grade system design including:
- JWT authentication (Cognito)  
- Async job queues  
- LLM-based output refinement  

---

## 📊 GitHub Stats
![GitHub Stats](https://github-stats-alpha.vercel.app/api?username=MrTig-afk&show_icons=true)

---

## ⚡ Fun Facts

- 🧩 Solved a Rubik's Cube in under 60 seconds  
- 🌱 Currently exploring **dbt + Airflow**  
- 🏏 Events Co-ordinator — RMIT Baseball Club  

---

## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kaushikn2002/) | [![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:kaushiknaru2002@gmail.com) | [![Medium](https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/@kaushiknaru2002)
