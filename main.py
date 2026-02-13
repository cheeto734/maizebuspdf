from maizeBusConvert import extract_classrooms
from maizeBusCord import export_Cords

# from maizeBusCord import ... TODO


def main():
    print("Extracting classroom IDs...")
    # In the future we go through all maps put in an array and run this multiple times but for now just Map.pdf
    extract_classrooms("Map.pdf")

    print("Extracting coordinates...")
    export_Cords("Map_Cropped.pdf")

    print("Done. Output written to classroomPos.json")


if __name__ == "__main__":
    main()


