from maizeBusConvert import extract_classrooms
from maizeBusCoord import export_Cords

def main():
    print("Extracting classroom IDs...")
    # In the future we go through all maps put in an array and run this multiple times but for now just Map.pdf
    extract_classrooms("Map.pdf")

    print("Extracting coordinates...")
    export_Cords("Map_Cropped.pdf", "classroomId.txt")

    print("Done. Output written to coords.json")


if __name__ == "__main__":
    main()


