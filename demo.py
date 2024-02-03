import math

from src.render_engine.rendering_api import LynRenderingApi as Lyn
from src.render_engine.primitives import *
from src.render_engine.compounds import *

api = Lyn()
api.init_window("Lyn Demo", 1000, 800)

# Scene 1
hello = Text("Hello, World!", 375, 1000, 40)
api.draw(hello)
api.move(hello, 375, 390, 0.5)
api.delay(1)
api.move(hello, 375, -220, 0.5)
del hello

# Scene 2
demo = Text("This is a demo for Lyn, the stupid little 'language'!", 65, 2000, 40)
api.draw(demo)
api.move(demo, 65, 390, 0.5)
api.delay(3)
api.move(demo, 65, -220, 0.5)
del demo

# Scene 3
features = Text("Let's see some features, shall we!", 200, -220, 40)
api.draw(features)
api.move(features, 200, 100, 0.5)

# Lines
api.delay(0.25)
line_text = Text("We've got lines:", 50, 200)
api.fade_in(line_text, 0.5)

line = Line(100, 230, 150, 500)
api.write_line(line, 1)

write_line = Text("And a write line animation!", 45, 540)
api.fade_in(write_line, 0.5)

# Rectangle
api.delay(0.25)
rect_text = Text("We've got rectangles:", 400, 200)
api.fade_in(rect_text, 0.5)

rect = Rectangle(400, 240, 200, 250, 5)
api.fade_in(rect, 0.5)

fade_in = Text("And a fade in animation!", 395, 540)
api.fade_in(fade_in, 0.5)

# Circles
api.delay(0.25)
circle_text = Text("And circles!", 800, 200)
api.fade_in(circle_text, 0.5)

circle = Circle(850, 360, 100, 5)
api.draw(circle)
api.delay(3)
backdrop = Rectangle(0, 0, 1000, 800, 0, fill=(40, 40, 40))
api.draw(backdrop)


def remove_backdrop():
    if backdrop in api.animated_objects:
        api.animated_objects.remove(backdrop)


# Scene 4
t1 = Text("It ain't much,", 255, 380, 60)
t2 = Text("but it's honest work.", 220, 380, 60)
t3 = Text("But wait, there's more!", 190, 380, 60)
t4 = Text("We've got graphs!", 100, 380, 100)

for t in (t1, t2, t3):
    api.delay(0.25)
    api.draw(t)
    api.delay(0.75)
    api.do(remove_backdrop)
    api.draw(backdrop)

api.delay(1)
api.draw(t4)
api.delay(2)
api.do(remove_backdrop)
api.draw(backdrop)
api.delay(1)

# Scene 5
api.do(lambda: api.animated_objects.clear())  # animation is getting slightly slow by this point
graph = Graph(500, 400, 15, 15, 15, 15, [
    lambda x: x ** 4,
    lambda x: math.sin(x),
    lambda x: -math.sin(x),
    lambda x: -(x ** 4)
])
api.draw(graph)

api.delay(2)
move_it_text = Text("And we can... move it, move it!", 100, 100)
api.fade_in(move_it_text)

api.move(graph, 300, 200, 0.25)
api.move(graph, 300, 600, 0.25)
api.move(graph, 500, 400, 0.25)
api.delay(3)

# The End
api.do(remove_backdrop)
api.fade_in(backdrop)
api.delay(1)
the_end = Text("The End (with a bug of course).", 200, 420, 40)
api.fade_in(the_end)

api.start_window_loop()
