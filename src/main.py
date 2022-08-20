from fastapi import FastAPI
from sqlalchemy import select

from database.make_engine import make_engine, make_engine
from database.setup_tables import Room, RoomCategory, Reservation

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/room")
async def room():
    stmt = select([
        Room.room_number,
        Room.category
    ])
    
    with make_engine().connect() as conn:
        results = conn.execute(stmt).fetchall()
    
    return results


@app.get("/room/{room_number}")
async def room_number(room_number: int):
    stmt = select([
        Room,
        RoomCategory.persons
    ]).join(RoomCategory).where(Room.room_number == room_number)
    
    with make_engine().connect() as conn:
        results = conn.execute(stmt).fetchall()
    
    return results


@app.get("/reservation")
async def all_reservation():
    stmt = select([Reservation]).join(Room).join(RoomCategory)
    
    with make_engine().connect() as conn:
        results = conn.execute(stmt).fetchall()
    
    return results


@app.get("/reservation/{reservation_number}")
async def reservation(reservation_number):
    stmt = select([Reservation]).join(Room).join(
        RoomCategory).where(Reservation.reservation_number == reservation_number)
    
    with make_engine().connect() as conn:
        results = conn.execute(stmt).fetchall()
    
    return results