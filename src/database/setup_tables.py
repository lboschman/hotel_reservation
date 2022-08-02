import sqlalchemy as db
from sqlalchemy import Column, ForeignKey, Integer, String, PickleType, insert, select, bindparam
from sqlalchemy.orm import declarative_base, relationship

from make_engine import make_engine

# Create table objects
Base = declarative_base()


class RoomCategory(Base):
    __tablename__ = "roomcategory"

    name = Column(String(64), primary_key=True)
    persons = Column(Integer)
    rooms = relationship("Room", backref="roomcategory")

    def __repr__(self) -> str:
        return f"<RoomCategory(name={self.name})>"


class Room(Base):
    __tablename__ = "room"

    number = Column(Integer, primary_key=True)
    category = Column(String(64), ForeignKey("roomcategory.name"))

    
    

# Create database engine
engine = make_engine(echo=True)
connection = engine.connect()


# Create the tables
Base.metadata.create_all(engine)