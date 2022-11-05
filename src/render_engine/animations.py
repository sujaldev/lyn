import math
from time import time as current_time

import skia


class Animation:
    def __init__(self, primitive):
        self.primitive = primitive

    def play(self, canvas: skia.Canvas, time: int) -> bool:
        pass


class Draw(Animation):
    def __init__(self, primitive):
        super().__init__(primitive)

    def play(self, canvas, _):
        self.primitive.render(canvas)
        return True


class FadeIn(Animation):
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
        percentage = math.sin(time / self.duration)

        if percentage >= 1:
            return True

        fill = list(self.primitive.fill)
        fill[-1] = int(percentage * self.fill_alpha)
        stroke = list(self.primitive.stroke_color)
        stroke[-1] = int(percentage * self.stroke_color)
        self.primitive.fill = tuple(fill)
        self.primitive.stroke_color = tuple(stroke)

        self.primitive.render(canvas)
        return False


class Delay(Animation):
    def __init__(self, duration):
        super().__init__(None)
        self.duration = duration
        self.start_time = None

    def play(self, canvas: skia.Canvas, time: int) -> bool:
        if self.start_time is None:
            self.start_time = time

        time = time - self.start_time
        return time >= self.duration
