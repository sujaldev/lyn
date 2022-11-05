import math
from src.render_engine.mathematics.bezier import ease

import skia


class Animation:
    def __init__(self, primitive):
        self.primitive = primitive

    def play(self, canvas: skia.Canvas, time: int) -> tuple:
        pass


class Draw(Animation):
    def __init__(self, primitive):
        super().__init__(primitive)

    def play(self, canvas, _):
        self.primitive.render(canvas)
        return True, self.primitive


class FadeIn(Animation):
    def __init__(self, primitive, duration=1):
        super().__init__(primitive)
        self.duration = duration

        self.fill_alpha = self.primitive.fill[-1] if self.primitive.fill[-1] else 255
        self.stroke_color = self.primitive.stroke_color[-1] if self.primitive.stroke_color[-1] else 255

        self.start_time = None

    def play(self, canvas, time):
        if self.start_time is None:
            self.start_time = time

        time = time - self.start_time
        percentage = math.sin(time / self.duration) if math.cos(time / self.duration) > 0 else 1

        if percentage >= 1:
            fill = list(self.primitive.fill)
            fill[-1] = 255
            stroke = list(self.primitive.stroke_color)
            stroke[-1] = 255
            self.primitive.fill = tuple(fill)
            self.primitive.stroke_color = tuple(stroke)
            self.primitive.render(canvas)
            return True, self.primitive

        fill = list(self.primitive.fill)
        fill[-1] = int(percentage * self.fill_alpha)
        stroke = list(self.primitive.stroke_color)
        stroke[-1] = int(percentage * self.stroke_color)
        self.primitive.fill = tuple(fill)
        self.primitive.stroke_color = tuple(stroke)

        self.primitive.render(canvas)
        return False, self.primitive


class FadeOut(Animation):
    def __init__(self, primitive, duration=3):
        super().__init__(primitive)
        self.duration = duration

        self.fill_alpha = self.primitive.fill[-1] if self.primitive.fill[-1] else 255
        self.stroke_color = self.primitive.stroke_color[-1] if self.primitive.stroke_color[-1] else 255

        self.start_time = None

    def play(self, canvas, time):
        if self.start_time is None:
            self.start_time = time

        time = time - self.start_time
        percentage = math.sin(time / self.duration) if math.cos(time / self.duration) > 0 else 1
        percentage = 1 - percentage

        if percentage <= 0:
            fill = list(self.primitive.fill)
            fill[-1] = 0
            stroke = list(self.primitive.stroke_color)
            stroke[-1] = 0
            self.primitive.fill = tuple(fill)
            self.primitive.stroke_color = tuple(stroke)
            self.primitive.render(canvas)
            return True, self.primitive

        fill = list(self.primitive.fill)
        fill[-1] = int(percentage * self.fill_alpha)
        stroke = list(self.primitive.stroke_color)
        stroke[-1] = int(percentage * self.stroke_color)
        self.primitive.fill = tuple(fill)
        self.primitive.stroke_color = tuple(stroke)

        self.primitive.render(canvas)
        return False, self.primitive


class Delay(Animation):
    def __init__(self, duration):
        super().__init__(None)
        self.duration = duration
        self.start_time = None

    def play(self, canvas, time):
        if self.start_time is None:
            self.start_time = time

        time = time - self.start_time
        return time >= self.duration, None


class Move(Animation):
    def __init__(self, primitive, x, y, duration=2):
        super().__init__(primitive)
        self.x_start, self.y_start = self.primitive.x, self.primitive.y
        self.x_end, self.y_end = x, y
        self.duration = duration
        self.start_time = None

    def play(self, canvas, time):
        if self.start_time is None:
            self.start_time = time

        time = time - self.start_time
        print(self.x_start, self.x_end, time, self.start_time + self.duration)
        self.primitive.x = ease(self.x_start, self.x_end, time, self.start_time + self.duration)
        self.primitive.y = ease(self.y_start, self.y_end, time, self.start_time + self.duration)

        if time >= self.start_time + self.duration:
            return True, self.primitive
        return False, self.primitive
