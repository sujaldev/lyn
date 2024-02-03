import skia
import src.render_engine.primitives as primitives

__all__ = ["Axis", "Graph"]


class Axis:
    UNIT_GAP = 50
    MARKING_HEIGHT = 10

    def __init__(self, x, y, units, horizontal=True, direction=1):
        self.x, self.y = x, y
        self.units = units
        self.horizontal = horizontal
        self.direction = 1 if direction >= 0 else -1

    def render_markings(self, canvas):
        canvas: skia.Canvas

        for i in range(1, self.units):
            if self.horizontal:
                x = self.x + self.UNIT_GAP * i * self.direction
                line = primitives.Line(
                    x, self.y - self.MARKING_HEIGHT / 2,
                    x, self.y + self.MARKING_HEIGHT / 2
                )
            else:
                y = self.y + self.UNIT_GAP * i * self.direction
                line = primitives.Line(
                    self.x - self.MARKING_HEIGHT / 2, y,
                    self.x + self.MARKING_HEIGHT / 2, y
                )
            line.render(canvas)

    def render(self, canvas):
        canvas: skia.Canvas
        if self.horizontal:
            number_line = primitives.Line(self.x, self.y, self.x + self.units * self.UNIT_GAP * self.direction, self.y)
        else:
            number_line = primitives.Line(self.x, self.y, self.x, self.y + self.units * self.UNIT_GAP * self.direction)
        number_line.render(canvas)
        self.render_markings(canvas)


class Graph:
    RESOLUTION = .01

    def __init__(self, x, y, x_units, y_units, negative_x_units, negative_y_units, equations):
        self.x, self.y = x, y
        self.x_units, self.y_units = x_units, y_units
        self.negative_x_units, self.negative_y_units = negative_x_units, negative_y_units
        self.equations = equations

        self.positive_x_axis = Axis(x, y, x_units)
        self.positive_y_axis = Axis(x, y, y_units, horizontal=False, direction=-1)
        self.negative_x_axis = Axis(x, y, negative_x_units, direction=-1)
        self.negative_y_axis = Axis(x, y, negative_y_units, horizontal=False)
        self.axes = (self.positive_x_axis, self.positive_y_axis, self.negative_x_axis, self.negative_y_axis)

    def render(self, canvas):
        self.positive_x_axis.render(canvas)
        self.positive_y_axis.render(canvas)
        self.negative_x_axis.render(canvas)
        self.negative_y_axis.render(canvas)

        for equation in self.equations:
            self.render_equation(canvas, equation)

    def render_equation(self, canvas, equation):
        conversion_num = self.positive_x_axis.UNIT_GAP
        x_end = self.x + self.x_units * conversion_num
        x_local = 0
        while self.x + x_local * conversion_num <= x_end:
            y_local = equation(x_local)
            next_x_local = x_local + self.RESOLUTION
            next_y_local = equation(next_x_local)

            canvas.drawLine(
                self.x + x_local * conversion_num, self.y - y_local * conversion_num,
                self.x + next_x_local * conversion_num, self.y - next_y_local * conversion_num,
                skia.Paint(Color=skia.ColorCYAN, StrokeWidth=2)
            )

            x_local += self.RESOLUTION

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if "axes" in self.__dict__.keys() and (key == 'x' or key == 'y'):
            for axis in getattr(self, "axes"):
                axis.__dict__[key] = value
