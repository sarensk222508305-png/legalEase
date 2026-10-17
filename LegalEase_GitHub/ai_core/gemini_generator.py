"""Gemini-powered legal document generation core."""

import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

try:
    import google.generativeai as genai
except ImportError:  # pragma: no cover
    genai = None


class GeminiDocumentGenerator:
    """Generate structured legal-document drafts with Gemini."""

    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY", "")
        self.model_name = model_name or os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
        self.model = None

        if self.api_key and genai is not None:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)

    @staticmethod
    def _prompt(document_type: str, parties: str, terms: str, dates: str) -> str:
        return f"""
You are LegalEase, an AI assistant for drafting educational legal-document templates.

Create a professional, structured draft for the following document.

Document type:
{document_type}

Parties involved:
{parties}

Effective date:
{dates}

Terms and conditions:
{terms}

Requirements:
- Use a clear title.
- Include the effective date.
- Identify the parties and their roles.
- Organize the document into logical sections.
- Include the supplied terms without inventing specific personal facts.
- Use formal, readable language.
- Add signature placeholders where appropriate.
- Return plain text suitable for later DOCX/PDF formatting.
- Do not claim that the draft is legally valid or jurisdiction-specific.
""".strip()

    def generate_document(
        self, document_type: str, parties: str, terms: str, dates: str
    ) -> str:
        if self.model is None:
            return self._demo_fallback(document_type, parties, terms, dates)

        response = self.model.generate_content(
            self._prompt(document_type, parties, terms, dates)
        )
        text = getattr(response, "text", None)
        if not text:
            raise RuntimeError("Gemini returned an empty response.")
        return text.strip()

    @staticmethod
    def _demo_fallback(document_type: str, parties: str, terms: str, dates: str) -> str:
        """Allow the UI to be demonstrated without exposing or requiring a key."""
        term_lines = [t.strip() for t in terms.split(";") if t.strip()]
        bullets = "\n".join(f"- {term}" for term in term_lines)
        return f"""# {document_type}

## Effective Date
{dates}

## Parties
{parties}

## Agreement
This educational template records the terms supplied by the user for the selected document type.

## Terms & Conditions
{bullets or "- No terms were supplied."}

## Signatures

Party 1: ______________________________

Party 2: ______________________________

Date: _________________________________

---
Educational draft generated in LegalEase demo mode. Obtain qualified legal review before real-world use.
"""
