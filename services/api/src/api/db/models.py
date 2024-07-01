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
    id = Column(Integer, primary_key=True)
    name = Column(String)
    symbol = Column(String)
    definition = Column(String)
    iri = Column(String)


class Quantity(Base):
    __tablename__ = "quantity"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    definition = Column(String)
    iri = Column(String)


class Class(Base):
    __tablename__ = "class"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    definition = Column(String)
    iri = Column(String)
