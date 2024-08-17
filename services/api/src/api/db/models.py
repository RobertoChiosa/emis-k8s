from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import PrimaryKeyConstraint

from src.api.db.database import Base


class Data(Base):
    __tablename__ = "data"

    time = Column(String, primary_key=True)
    value = Column(Integer, primary_key=True)
    uuid = Column(String)

    # primary key composite
    __table_args__ = (
        PrimaryKeyConstraint('time', 'value'),
    )
