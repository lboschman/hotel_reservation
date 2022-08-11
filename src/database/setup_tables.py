import sqlalchemy as db
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import declarative_base, relationship

from database.make_engine import make_engine

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

    room_number = Column(Integer, primary_key=True)
    category = Column(String(64), ForeignKey("roomcategory.name"))


class Reservation(Base):
    __tablename__ = "reservation"

    reservation_number = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    start_date = Column(Date)
    end_date = Column(Date)
    

if __name__=="__main__":
    # Create database engine
    engine = make_engine(echo=True)
    connection = engine.connect()


    # Create the tables
    Base.metadata.create_all(engine)

    connection.close()