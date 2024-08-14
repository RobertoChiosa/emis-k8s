from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.api.db import schemas
from src.api.db.database import get_db

router = APIRouter(
    prefix="/metadata",
    tags=["Metadata"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    path="/data/",
    summary="Get data",
    tags=["Metadata"],
    response_model=list[schemas.Data]
)
def get_data(db: Session = Depends(get_db)):
    """
    Get all meters
    :param db: The database session
    :return:  All meters
    """

    return {}
