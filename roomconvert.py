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

# Classifying Rooms + Finding what is a classroom
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
    
    if re.fullmatch(r"\d[A-Z]\d{2}", room_name):
        return RoomType.HALLWAY
    
    if re.fullmatch(r"\d{4}-[A-Z]", room_name):
        return RoomType.CLASSROOM
    
    if re.fullmatch(r"\d{4}", room_name):
        return RoomType.WORK_SPACE
    
    if re.fullmatch(r"\d{4}-\d{2}", room_name):
        return RoomType.CLASSROOM

@dataclass
class Room:
    name: str
    location: tuple
    classification: RoomType

def export_classrooms_to_file(rooms, filename="classroomId.txt"):
    with open(filename, "w") as file:  # "w" overwrites file each time
        for room in rooms:
            if room.classification == RoomType.CLASSROOM:
                file.write(f"{room.name}\n")

    print(f"Classroom IDs written to {filename}")


# This is for finding the Position of Rooms
doc = fitz.open("Map.pdf")
print(type(doc))
room_directory = dict()
# page = .txt file
for page in doc: # Instead of page in doc, we need to say text file in doc to get the correct rooms
    text = page.TextPage.extractTEXT().splitlines()
    sPrint = 0
    for line in text:
        if sPrint == 2:
            print(line)
            tempClasser = RoomType.CLASSROOM
            room_directory[line] = Room(line, (0, 0), tempClasser)
        elif len(line) > 5 and line[2] == "/" and line[5] == "/":
            sPrint += 1
doc.close()


class Cords:
  def __init__(self):
    self.x0 = 0
    self.y0 = 0
    self.name = ""


doc = fitz.open("Map_Cropped.pdf")
page = doc[0]

#x0, y0, x1, y1, Room
words = page.get_text("words")

rooms = []
for i in range(len(words)):
  room = Cords()
  room.x0 = (words[i][0] + words[i][2])/2
  room.y0 = (words[i][1] + words[i][3])/2
  room.name = words[i][4]
  rooms.append(room)

for room in rooms:
  for i in range(len(rooms)):
    print("Location name:", rooms[i].name)
    print("X coordinate", rooms[i].x0)
    print("Y coordinate", rooms[i].y0)
    print("Next Location: ")

# Output to classroomPos.json file with roomID, X/Y Coordinate
