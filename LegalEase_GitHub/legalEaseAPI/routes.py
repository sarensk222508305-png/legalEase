from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ai_core.gemini_generator import GeminiDocumentGenerator
from utils.text_utils import sanitize_text

router = APIRouter()
gemini_generator = GeminiDocumentGenerator()


class DocumentRequest(BaseModel):
    document_type: str = Field(..., min_length=2, max_length=120)
    parties: str = Field(..., min_length=2, max_length=2000)
    terms: str = Field(..., min_length=2, max_length=6000)
    dates: str = Field(..., min_length=2, max_length=100)


@router.post("/generate")
def generate_legal_document(request: DocumentRequest):
    try:
        response = gemini_generator.generate_document(
            request.document_type,
            request.parties,
            request.terms,
            request.dates,
        )
        return {"document": sanitize_text(response)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
