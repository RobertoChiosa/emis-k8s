#  Copyright © Roberto Chiosa 2024.
#  Email: roberto.chiosa@polito.it
#  Last edited: 4/10/2024

# Standard library imports
import io

# Third party imports
from fastapi import APIRouter, Request, Response
from fastapi.templating import Jinja2Templates

# Project imports
from src.api.utils.utils_report import (
    generate_test_report_html,
    generate_test_report_pdf,
    generate_test_report_word,
)

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/report",
    tags=["Report"],
    responses={404: {"description": "Not found"}},
)


@router.get("/test/pdf")
def test_report_pdf():
    """
    Generate a test PDF report
    """
    out = generate_test_report_pdf().output("output_file.pdf", "S").encode("latin-1")
    headers = {
        "Content-Disposition": 'inline; filename="output_file.pdf"',
        "Content-Encoding": "UTF-8",
    }
    return Response(bytes(out), headers=headers, media_type="application/pdf")


@router.get("/test/html")
async def test_report_html(request: Request):
    """
    Generate a test HTML report
    """
    content = generate_test_report_html()
    return templates.TemplateResponse(
        request=request, name="diagnostic.html", context=content
    )


@router.get("/test/docx")
async def test_report_word():
    """
    Generate a test DOCX report
    """
    out = generate_test_report_word()
    # save document info
    buffer = io.BytesIO()
    out.save(buffer)  # save your memory stream
    buffer.seek(0)  # rewind the stream

    headers = {
        "Content-Disposition": 'inline; filename="output_file.pdf"',
        "Content-Encoding": "UTF-8",
    }
    return Response(
        buffer.encode("utf-8"),
        headers=headers,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
