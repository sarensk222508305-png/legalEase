# Phase 7 — Project Documentation

## Purpose
LegalEase is designed to make structured legal-document drafting more accessible through a guided interface and generative AI.

## Technology Stack
- Python
- FastAPI
- Streamlit
- Google Gemini
- Pydantic
- python-docx
- FPDF2
- Requests
- python-dotenv

## Installation
See the root `README.md`.

## API

### `GET /`
Returns service status.

### `POST /generate`
Request:
```json
{
  "document_type": "Freelance Work Contract",
  "parties": "Jane Doe (Service Provider), TechNova Inc. (Client)",
  "terms": "Payment within 30 days; Confidentiality must be maintained",
  "dates": "April 15, 2025"
}
```

Response:
```json
{
  "document": "..."
}
```

## User Guide
1. Start FastAPI.
2. Start Streamlit.
3. Enter document details.
4. Generate.
5. Review/edit.
6. Download.

## Limitations
- AI output can contain errors.
- Legal requirements differ by jurisdiction.
- The academic prototype does not provide legal advice.
- A valid Gemini API key is needed for live AI generation.

## Future Enhancements
The supplied project conclusion suggests deeper contract analysis, legal-database integration and personalized recommendations as possible future enhancements.
