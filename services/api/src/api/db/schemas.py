from typing import Optional

from fastapi import Body
from pydantic import BaseModel


class Meter(BaseModel):
    """Response model for dataloggers"""
    id: int = Body(
        title='id',
        description='The meter unique identifier',
    )
    description: str = Body(
        title='Description of the meter',
        description='Description of the meter as it is on the datalogger with convention "ID>] DESC"',
    )
    type_id: Optional[str] = Body(
        title='Type ID',
        description='The type ID of the meter represented as BRICK class',
    )
    unit_id: Optional[str] = Body(
        title='Unit ID',
        description='The unit ID of the meter represented as QUDT unit',
    )
    quantity_id: Optional[str] = Body(
        title='Quantity ID',
        description='The quantity ID of the meter represented as QUDT quantityKind',
    )

    # class Config:
    #     orm_mode = True

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 860,
                    "description": "860] Attiva GME",
                    "type_id": "Active_Power_Sensor",
                    "unit_id": "KiloW",
                    "quantity_id": "ElectricPower"
                }
            ]
        }
    }
