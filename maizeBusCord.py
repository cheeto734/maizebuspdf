import fitz

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
