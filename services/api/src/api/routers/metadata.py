from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.api.db.database import get_db

router = APIRouter(
    prefix="/metadata",
    tags=["Metadata"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    path="",
    summary="Get all meters",
    tags=["Monitoring"],
    # response_model=list[schemas.Meter]
)
def get_metadata_meters_all(db: Session = Depends(get_db)):
    """
    Get all meters
    :param db: The database session
    :return:  All meters
    """
    return {}
