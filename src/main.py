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
    engine = make_engine()
    conn = engine.connect()
    results = conn.execute(stmt).fetchall()
    return results

