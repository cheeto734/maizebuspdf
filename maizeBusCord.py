import fitz
import json

class Cords:
  def __init__(self):
    self.x0 = 0
    self.y0 = 0
    self.name = ""





def export_Cords(file_name):
  doc = fitz.open(file_name)

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

  data = {}
  for room in rooms:
    data[room.name] = (room.x0, room.y0)

  with open("cords.json", "w") as f:
    json.dump(data, f, indent=4)

