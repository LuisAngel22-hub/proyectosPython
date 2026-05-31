import turtle
import json


#ES DE LO DEL INSTA QUE VI EL LAIK
def draw_from_json(json_file):
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(800, 800)
    t= turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    screen.tracer(0)

    with open (json_file) as f:
        regions= json.load(f)

        all_points = [(p[0],p[1]) for r in regions
                      for p in r['contour']]
    min_x= min (p[0] for p in all_points)
    max_x= max (p[0] for p in all_points)
    min_y= min (p[1] for p in all_points)
    max_y= max (p[1] for p in all_points)

    width = max_x - min_x
    height = max_y - min_y
    scale = min(700/width, 600/height)
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    #Dibuja la region