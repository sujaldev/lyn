import skia
from src.render_engine.ui_backend import Window
import src.render_engine.animations as animations


class LynRenderingApi:
    def __init__(self):
        self.window = None
        self.animation_queue = []
        self.animated_objects = []

    def init_window(self, title, width, height, x=None, y=None, flags=None):
        self.window = Window(title, width, height, x, y, flags)
        self.window.frame_renderer = self.frame_renderer

    def start_window_loop(self):
        if self.window:
            self.animation_queue = list(reversed(self.animation_queue))
            self.window.main_loop()
        else:
            raise Exception("Initialize window before calling start_window_loop()")

    def frame_renderer(self, canvas, time):
        canvas: skia.Canvas
        canvas.drawColor(skia.Color(*self.window.canvas_color))
        for obj in self.animated_objects:
            if obj is not None:
                obj.render(canvas)

        if not self.animation_queue:
            return

        current_animation = self.animation_queue[-1]
        if callable(current_animation):
            self.animation_queue[-1] = self.animation_queue[-1]()

        if self.animation_queue[-1] is None:
            self.animation_queue.pop()
            return

        animation_complete, completed_obj = self.animation_queue[-1].play(canvas, time)
        if animation_complete:
            self.animation_queue.pop()
            if completed_obj is not None and completed_obj not in self.animated_objects:
                self.animated_objects.append(completed_obj)

    def draw(self, primitive):
        self.animation_queue.append(lambda: animations.Draw(primitive))

    def write_line(self, primitive, duration=2):
        self.animation_queue.append(lambda: animations.WriteLine(primitive, duration))

    def fade_in(self, primitive, duration=1):
        self.animation_queue.append(lambda: animations.FadeIn(primitive, duration))

    def fade_out(self, primitive, duration=1):
        self.animation_queue.append(lambda: animations.FadeOut(primitive, duration))

    def delay(self, duration=1):
        self.animation_queue.append(lambda: animations.Delay(duration))

    def move(self, primitive, x, y, duration=2):
        self.animation_queue.append(lambda: animations.Move(primitive, x, y, duration))

    def do(self, func):
        # Quick fix to allow sequential execution
        self.animation_queue.append(func)
