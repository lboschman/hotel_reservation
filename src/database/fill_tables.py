from calendar import month
from database.setup_tables import Reservation, Room, RoomCategory
from database.make_engine import make_engine

from sqlalchemy import insert, table
from datetime import date

categories = [
    {
        "name": "FamilyRoom",
        "persons": 4,
    },
    {
        "name": "DoubleRoom",
        "persons": 2
    }
]

fam_rooms = [{
    "room_number": i, 
    "category": "FamilyRoom"
    } for i in range(102, 128)]
dbl_rooms  = [{
    "room_number": i, 
    "category": "DoubleRoom"
    } for i in range(202, 228)]

reservations = [
    {
        "reservation_number": 1,
        "name": "Boschman",
        "start_date": date(year=2022, month=8, day=5),
        "end_date": date(year=2022, month=8, day=5),
        "room": 205
    }
]


engine = make_engine(local=True)

with engine.connect() as conn:
    result = conn.execute(
        insert(RoomCategory),
        categories
    )

    result = conn.execute(
        insert(Room),
        fam_rooms + dbl_rooms
    )

    result = conn.execute(
        insert(Reservation),
        reservations
    )

