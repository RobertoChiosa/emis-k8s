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

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/report",
    tags=["Report"],
    responses={404: {"description": "Not found"}},
)


def get_context():
    """
    Get the context for the report
    :return:
    """
    context = {
        'title': 'Report',
        'subtitle': 'Report',
        'summary': {
            'title': 'Summary',
            'content': 'The aim of this report is to analyze the data quality related to a specific meter id.'
        },
        'metadata': {
            'title': 'Metadata',
            'content': 'The aim of this report is to analyze the data quality related to a specific meter id.'
        },
        'data': {
            'title': 'Data',
            'content': 'The aim of this report is to analyze the data quality related to a specific meter id.'
        },
    }
    return context


@router.get("/{type}")
async def report_diagnostic_meter(
        request: Request,
        type: str
):
    """
    Report that contains info related to a meter id
    :param request:
    :param id:
    :return:
    """
    # if pdf do pdf
    # if word do word
    # if html do html
    context = get_context()
    return templates.TemplateResponse(
        request=request, name="diagnostic.html", context=context
    )
