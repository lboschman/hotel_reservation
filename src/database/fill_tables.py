from database.setup_tables import Room, RoomCategory
from database.make_engine import make_engine

from sqlalchemy import insert, table

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

engine = make_engine()

with engine.connect() as conn:
    result = conn.execute(
        insert(RoomCategory),
        categories
    )

    result = conn.execute(
        insert(Room),
        fam_rooms + dbl_rooms
    )


