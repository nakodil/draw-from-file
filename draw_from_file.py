import turtle as t
import sys


def get_coordinates(file: str) -> list:
    try:
        source_file = open(file, "r", encoding='utf-8')
    except:
        print("Невозможно открыть или прочитать файл.")
        sys.exit()
   
    file_lines = source_file.read().splitlines()
    
    coordinates_list = []
    for line_index, line in enumerate(file_lines):
        for symbol_index, symbol in enumerate(line):
            coordinates_list.append((line_index, symbol_index, symbol))
    
    source_file.close()
    return coordinates_list


def stamp(coordinates: list):
    for i in coordinates:
        x = i[1] * 20  # hardcoded!
        y = i[0] * -20
        c = i[2]
        if c == "0":
            color = "red"
        elif c == "1":
            color = "green"
        elif c == "2":
            color = "blue"
        else:
            print("unknown color, setting black instead")
            color = "black"
        t.color(color)
        t.goto(x, y)
        t.stamp()
        print("stamp at", x, y, color)
    

# setup
t.penup()
t.speed(-1)
t.pensize(10)
t.shape("square")
t.goto(0, 0)

coordinates_list = get_coordinates("source.txt")
stamp(coordinates_list) 
t.done()
