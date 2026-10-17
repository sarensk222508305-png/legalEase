# Phase 2 — Requirement Analysis

## Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | Accept legal document type |
| FR-02 | Accept parties and roles |
| FR-03 | Accept terms and conditions |
| FR-04 | Accept effective date |
| FR-05 | Generate document using Gemini |
| FR-06 | Display generated content |
| FR-07 | Allow editing of generated content |
| FR-08 | Download TXT |
| FR-09 | Download DOCX |
| FR-10 | Download PDF |
| FR-11 | Provide FastAPI `/generate` endpoint |
| FR-12 | Provide API health/root endpoint |

## Non-Functional Requirements
- Usable Streamlit interface
- Clear validation messages
- Modular backend architecture
- Environment-variable based API-key configuration
- Reasonable document formatting
- Maintainable Python source structure
- No secret credentials committed to GitHub

## Inputs
`document_type`, `parties`, `terms`, `dates`

## Outputs
AI-generated/editable legal-document text and TXT/DOCX/PDF files.

## Technical Requirements
The supplied project document identifies Python, FastAPI, Streamlit, Gemini, python-docx, FPDF, Pillow, requests and python-dotenv as the main technologies/dependencies.
