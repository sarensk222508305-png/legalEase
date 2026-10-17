# LegalEase — AI-Powered Legal Document Generator

LegalEase is a FastAPI + Streamlit application that uses Google Gemini to generate customizable legal-document drafts from user-provided document type, parties, terms, and effective date. Generated content can be previewed, edited, and exported as TXT, DOCX, or PDF.

> **Important:** LegalEase is an educational/project prototype. AI-generated text is not a substitute for advice or review by a qualified legal professional.

## Project requirements covered
- FastAPI backend with `POST /generate`
- Streamlit frontend
- Gemini integration
- Editable generated-document preview
- TXT, DOCX and PDF exports
- Basic branded document formatting
- Phase-wise project documentation
- Test cases and demo script

The implementation follows the supplied SmartBridge LegalEase project document, which specifies Streamlit, FastAPI, Gemini, and DOCX/PDF/TXT export workflows. See `docs/` for all eight required phases.

## Repository structure

```text
LegalEase/
├── ai_core/
│   └── gemini_generator.py
├── legalEaseAPI/
│   ├── main.py
│   └── routes.py
├── frontend/
│   └── app.py
├── utils/
│   ├── document_formatter.py
│   └── text_utils.py
├── assets/
│   └── README.md
├── tests/
│   └── test_api.py
├── docs/
│   ├── 01_Brainstorming_Ideation/
│   ├── 02_Requirement_Analysis/
│   ├── 03_Project_Design/
│   ├── 04_Project_Planning/
│   ├── 05_Project_Development/
│   ├── 06_Project_Testing/
│   ├── 07_Project_Documentation/
│   └── 08_Project_Demonstration/
├── .env.example
├── .gitignore
├── requirements.txt
├── run_backend.py
└── README.md
```

## 1. Setup

Python 3.10+ is recommended.

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Windows
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Open `.env` and set your Gemini API key.

## 2. Run the backend

```bash
python run_backend.py
```

The API runs at `http://127.0.0.1:8000`.

Health check:
```text
GET http://127.0.0.1:8000/
```

API documentation:
```text
http://127.0.0.1:8000/docs
```

## 3. Run the frontend

Open another terminal with the virtual environment activated:

```bash
streamlit run frontend/app.py
```

The Streamlit UI will open in the browser.

## 4. Typical workflow

1. Enter a document type such as `Employment Contract`, `NDA`, or `Lease Agreement`.
2. Enter the parties and their roles.
3. Enter terms separated by semicolons.
4. Enter the effective date.
5. Click **Generate Document**.
6. Review the AI-generated draft.
7. Edit the draft if required.
8. Download TXT, DOCX, or PDF.

## 5. Security notes

- Never commit `.env` or a real API key.
- Use `.env.example` as the public configuration template.
- Treat user-entered legal information as sensitive.
- Do not upload confidential client information to a public demo.
- Validate request data at the API boundary.
- Review generated legal content before real-world use.

## 6. Demo data

Use fictional data for demonstrations. Example:
- Document type: Freelance Work Contract
- Parties: Jane Doe (Service Provider), TechNova Inc. (Client)
- Terms: Payment within 30 days; Confidentiality must be maintained; Either party may terminate with 15 days notice
- Effective date: April 15, 2025

## 7. Source alignment

The supplied project document describes LegalEase as an AI-powered legal document generator supporting contracts, NDAs, lease agreements and similar documents, with editable previews and TXT/DOCX/PDF export. It specifies Streamlit for the frontend, FastAPI for the backend, and Gemini for generation.

## License

This repository is prepared as an academic project submission. Add your institution/team's preferred license if required.
