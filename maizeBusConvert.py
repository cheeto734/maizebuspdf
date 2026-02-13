# import fitz
# source venv/bin/activate to run in venv
# switch environment to venv at bottom right
# deactivate to exit venv
# pip install pymupdf pyinstaller
# add ., status, commit -m "commit msg", add
import fitz
import re
from dataclasses import dataclass
from enum import Enum


class RoomType(Enum):
    CLASSROOM = "Classroom"
    AUDITORIUM = "Auditorium"
    HALLWAY = "Hallway"
    BATHROOM = "Bathroom"
    CLOSET = "Closet"
    OFFICE = "Office"
    WORK_SPACE = "Work Space"
    STAIRWAY = "Stairway"
    ELEVATOR = "Elevator"

pattern_mapping = [
    (r"\d[A-Z]\d{2}", RoomType.HALLWAY),
    (r"\d{4}-[A-Z]", RoomType.CLASSROOM),
    (r"\d{4}", RoomType.WORK_SPACE),
    (r"\d{4}-\d{2}", RoomType.CLASSROOM),
]

def classify_room(room_name: str) -> RoomType:
    
    if re.fullmatch(r"\d[A-Z]\d{2}", room_id):
        return RoomType.HALLWAY
    
    if re.fullmatch(r"\d{4}-[A-Z]", room_id):
        return RoomType.CLASSROOM
    
    if re.fullmatch(r"\d{4}", room_id):
        return RoomType.WORK_SPACE
    
    if re.fullmatch(r"\d{4}-\d{2}", room_id):
        return RoomType.CLASSROOM

@dataclass
class Room:
    name: str
    location: tuple
    classification: RoomType



print("hello world")


doc = fitz.open("Map.pdf")
print(type(doc))
room_directory = dict()

for page in doc:
    text = page.get_text().splitlines()
    sPrint = 0
    for line in text:
        if sPrint == 2:
            print(line)
            tempClasser = RoomType.CLASSROOM
            room_directory[line] = Room(line, (0, 0), tempClasser)
        elif len(line) > 5 and line[2] == "/" and line[5] == "/":
            sPrint += 1
doc.close()


