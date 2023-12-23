import turtle as tu
import re
import docx
import os

source_folder = "coordinates"  # source folder where the coordinates files are stored
source_filename = "panda"  # source filename without extension

# Construct the full path to the Word document in the coordinates folder
source_path = os.path.join(source_folder, "{}.docx".format(source_filename))

data = docx.Document(source_path)
coordinates = []
colour = []

for i in data.paragraphs:
    try:
        coord_stg_tup = re.findall(r'\([-+]?\d*\.\d*(?:[eE][-+]?\d+)? ?\, ?[-+]?\d*\.\d*(?:[eE][-+]?\d+)?\)', i.text)
        coord_num_tup = []
        color_stg_tup = re.findall(r'\([-+]?\d*\.\d*(?:[eE][-+]?\d+)? ?\, ?[-+]?\d*\.\d*(?:[eE][-+]?\d+)? ?\, ?[-+]?\d*\.\d*(?:[eE][-+]?\d+)?\)', i.text)
        color_val = re.findall(r'[-+]?\d*\.\d*', color_stg_tup[0])
        color_val_lst = [float(k) for k in color_val]
        colour.append(tuple(color_val_lst))

        for j in coord_stg_tup:
            coord_pos = re.findall(r'[-+]?\d*\.\d*', j)
            coord_num_lst = [float(k) for k in coord_pos]
            coord_num_tup.append(tuple(coord_num_lst))

        coordinates.append(coord_num_tup)
    except:
        pass

pen = tu.Turtle()
screen = tu.Screen()
screen.screensize(900, 900)
tu.tracer(10)
tu.hideturtle()
pen.speed(0)

for i in range(len(coordinates)):
    draw = 1
    path = coordinates[i]
    col = colour[i]
    pen.color(col)
    pen.begin_fill()
    for order_pair in path:
        x, y = order_pair
        y = -1 * y
        if draw:
            pen.up()
            pen.goto(x, y)
            pen.down()
            draw = 0
        else:
            pen.goto(x, y)
    pen.end_fill()
    pen.hideturtle()

screen.mainloop()
