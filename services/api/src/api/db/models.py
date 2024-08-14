from sqlalchemy import Column, Integer, String

from src.api.db.database import Base


class Data(Base):
    __tablename__ = "data"

    time = Column(String, index=True)
    value = Column(Integer, index=True)
    uuid = Column(String)
