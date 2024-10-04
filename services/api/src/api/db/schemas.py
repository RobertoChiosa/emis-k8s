# Third party imports
from fastapi import Body
from pydantic import BaseModel


class Data(BaseModel):
    """Response model for dataloggers"""

    time: str = Body(
        title="time",
        description="The time of the data",
    )
    value: float = Body(
        title="value",
        description="The value of the data",
    )
    uuid: str = Body(
        title="uuid",
        description="The unique identifier of the meter",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"time": "2021-01-01T00:00:00", "value": 123.45, "uuid": "12345678-123"}
            ]
        }
    }
