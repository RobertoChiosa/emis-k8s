"""
Author:       Roberto Chiosa
Copyright:    Roberto Chiosa, © 2024
Email:        roberto.chiosa@pinvision.it

Created:      04/06/24
Script Name:  report.py
Path:         src/api/routers

Script Description:


Notes:
"""
import io

from fastapi import APIRouter, Request
from fastapi import Response
from fastapi.templating import Jinja2Templates

from src.api.utils_report import generate_test_report_pdf, generate_test_report_word, generate_test_report_html

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
    :return:
    """
    out = generate_test_report_pdf().output("output_file.pdf", 'S').encode('latin-1')
    headers = {
        'Content-Disposition': 'inline; filename="output_file.pdf"',
        'Content-Encoding': 'UTF-8'
    }
    return Response(bytes(out), headers=headers, media_type='application/pdf')


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
        'Content-Disposition': 'inline; filename="output_file.pdf"',
        'Content-Encoding': 'UTF-8'
    }
    return Response(buffer.encode("utf-8"), headers=headers,
                    media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
