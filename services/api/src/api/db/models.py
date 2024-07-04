from sqlalchemy import Column, Integer, String, ForeignKey

from src.api.db.database import Base


class Meter(Base):
    __tablename__ = "meter"
    id = Column(Integer, primary_key=True)
    description = Column(String)
    type_id = Column(Integer, ForeignKey("class.id"))
    quantity_id = Column(Integer, ForeignKey("quantity.id"))
    unit_id = Column(Integer, ForeignKey("unit.id"))


class Unit(Base):
    __tablename__ = "unit"
    name = Column(String, primary_key=True)
    symbol = Column(String)
    definition = Column(String)
    iri = Column(String)


class Quantity(Base):
    __tablename__ = "quantity"
    name = Column(String, primary_key=True)
    definition = Column(String)
    iri = Column(String)


class Class(Base):
    __tablename__ = "class"
    name = Column(String, primary_key=True)
    definition = Column(String)
    iri = Column(String)
