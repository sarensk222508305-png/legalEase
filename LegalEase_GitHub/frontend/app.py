import os
import html
import requests
import streamlit as st
from dotenv import load_dotenv

from utils.document_formatter import format_docx, format_pdf, format_txt

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")

st.set_page_config(page_title="LegalEase", page_icon="⚖️", layout="centered")

st.markdown(
    """
    <style>
    .hero { text-align:center; padding: 0.6rem 0 1rem; }
    .hero h1 { margin-bottom:0.1rem; }
    .card { padding:1rem; border-radius:14px; border:1px solid rgba(128,128,128,.25); }
    .disclaimer { font-size:.82rem; opacity:.78; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="hero"><h1>⚖️ LegalEase</h1><p>AI-Powered Legal Document Generator</p></div>', unsafe_allow_html=True)

st.info(
    "Educational prototype: generated text should be reviewed by a qualified legal professional before real-world use."
)

with st.form("legal_form"):
    document_type = st.text_input(
        "Document Type",
        placeholder="e.g., Freelance Work Contract",
    )
    parties = st.text_area(
        "Parties Involved",
        placeholder="e.g., Jane Doe (Service Provider), TechNova Inc. (Client)",
        height=90,
    )
    terms = st.text_area(
        "Terms & Conditions",
        placeholder="Use semicolons between clauses: Payment within 30 days; Confidentiality must be maintained",
        height=130,
    )
    dates = st.text_input(
        "Effective Date",
        placeholder="e.g., April 15, 2025",
    )
    submitted = st.form_submit_button("✨ Generate Document", use_container_width=True)

if submitted:
    missing = []
    for label, value in [
        ("Document Type", document_type),
        ("Parties Involved", parties),
        ("Terms & Conditions", terms),
        ("Effective Date", dates),
    ]:
        if not value.strip():
            missing.append(label)

    if missing:
        st.error("Please complete: " + ", ".join(missing))
    else:
        with st.spinner("Generating your document..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/generate",
                    json={
                        "document_type": document_type,
                        "parties": parties,
                        "terms": terms,
                        "dates": dates,
                    },
                    timeout=120,
                )
                response.raise_for_status()
                st.session_state.generated_text = response.json()["document"]
                st.session_state.doc_type = document_type
                st.success("Document generated successfully.")
            except requests.RequestException as exc:
                st.error(f"Could not reach the FastAPI backend: {exc}")

if "generated_text" in st.session_state:
    st.subheader("📄 Document Generated")
    edited = st.text_area(
        "Edit Document Below",
        value=st.session_state.generated_text,
        height=420,
        key="editable_document",
    )
    st.session_state.generated_text = edited

    st.subheader("Preview")
    preview = html.escape(edited).replace("\n", "<br>")
    st.markdown(
        f'<div class="card">{preview}</div>',
        unsafe_allow_html=True,
    )

    doc_type = st.session_state.get("doc_type", "Legal Document")
    st.download_button(
        "⬇️ Download as TXT",
        data=format_txt(edited),
        file_name=f"{doc_type.replace(' ', '_')}.txt",
        mime="text/plain",
        use_container_width=True,
    )
    st.download_button(
        "⬇️ Download as DOCX",
        data=format_docx(edited, doc_type),
        file_name=f"{doc_type.replace(' ', '_')}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        use_container_width=True,
    )
    st.download_button(
        "⬇️ Download as PDF",
        data=format_pdf(edited, doc_type),
        file_name=f"{doc_type.replace(' ', '_')}.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

st.caption("LegalEase • SmartBridge academic project implementation")
