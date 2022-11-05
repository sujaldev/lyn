import skia
import sdl2 as sdl
from src.render_engine.ui_backend import Window
import src.render_engine.animations as animations
import src.render_engine.primitives as primitives


class LynRenderingApi:
    def __init__(self):
        self.window = None
        self.animation_queue = []

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
        if not self.animation_queue:
            self.window.frame_renderer = None
            return

        animation_complete = self.animation_queue[-1].play(canvas, time)
        if animation_complete:
            self.animation_queue.pop()

    def draw(self, primitive):
        self.animation_queue.append(animations.Draw(primitive))

    def fade_in(self, primitive, duration=3):
        self.animation_queue.append(animations.FadeIn(primitive, duration))

    def delay(self, duration=1):
        self.animation_queue.append(animations.Delay(duration))
