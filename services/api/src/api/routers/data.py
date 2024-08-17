from datetime import datetime

from fastapi import APIRouter, Query
from fastapi import Depends
from requests import Session
from src.api.db import models
from src.api.db.database import get_db

router = APIRouter(
    prefix="/data",
    tags=["Monitoring"],
    responses={404: {"description": "Not found"}}
)


@router.get(path="",
            tags=["Monitoring"],
            summary="Get time-series given uuid and time range",
            )
async def get_data_meter_id(
        db: Session = Depends(get_db),
        uuid: list[str] = Query(
            default=['860'],
            title='uuid',
            description='The unique identifier of the meter',
            examples=['860', '9000']
        ),
        start_datetime: datetime = Query(
            default=datetime(2024, 6, 17),
            title='Start datetime',
            description='First timestamp of the query',
            examples=['2024-07-01T01:15:00Z']
        ),
        end_datetime: datetime = Query(
            default=datetime(2024, 6, 21),
            title='End datetime',
            description='Last timestamp of the query',
            examples=['2024-07-02T04:15:00Z']
        )
):
    res = (db.query(models.Data).where(
        models.Data.uuid.in_(uuid),
        models.Data.time.between(start_datetime, end_datetime)
    ).order_by(models.Data.time).all())

    return res
