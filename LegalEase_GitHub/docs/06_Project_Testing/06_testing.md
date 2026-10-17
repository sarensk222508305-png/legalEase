# Phase 6 — Project Testing

## Test Plan

| TC ID | Test | Expected Result |
|---|---|---|
| TC-01 | Open `/` | API returns running status |
| TC-02 | Submit valid document data | Generation endpoint returns `document` |
| TC-03 | Leave document type empty in UI | Validation error |
| TC-04 | Leave parties empty | Validation error |
| TC-05 | Leave terms empty | Validation error |
| TC-06 | Leave date empty | Validation error |
| TC-07 | Generate document | Editable output appears |
| TC-08 | Edit generated text | Edited content remains available |
| TC-09 | Download TXT | `.txt` file downloads |
| TC-10 | Download DOCX | `.docx` file downloads |
| TC-11 | Download PDF | `.pdf` file downloads |
| TC-12 | Run without Gemini key | Demo fallback permits local UI testing |
| TC-13 | API receives oversized input | Validation rejects invalid request |
| TC-14 | Check API docs | FastAPI Swagger UI opens at `/docs` |

## Automated Tests
`tests/test_api.py` covers the root endpoint and the generation endpoint.

Run:
```bash
pip install -r requirements.txt
pytest -q
```

## Manual Testing
Use the fictional sample data from `README.md`. Verify that the same edited text is reflected in TXT/DOCX/PDF downloads.

## Security Checks
- Confirm `.env` is ignored by Git.
- Confirm no API key is present in source files.
- Use fictional data in demos.
- Verify input validation.
