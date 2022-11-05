import skia


class Rectangle:
    def __init__(self, x, y, width, height, stroke_width=20, stroke_color=(255, 86, 128, 255),
                 fill=(199, 199, 199, 255)):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.stroke_width = stroke_width
        self.stroke_color = stroke_color
        self.fill = fill

    def render_border(self, canvas):
        canvas: skia.Canvas
        paint = skia.Paint(StrokeWidth=self.stroke_width, Color=skia.Color(*self.stroke_color))
        half_stroke_width = self.stroke_width / 2
        x1 = int(self.x - half_stroke_width)
        x2 = x1 + self.width + self.stroke_width
        y1 = int(self.y - half_stroke_width)
        canvas.drawLine(x1, self.y, x1, self.y + self.height, paint)  # right border
        canvas.drawLine(x2, self.y, x2, self.y + self.height, paint)  # left border
        canvas.drawLine(x1 - half_stroke_width, y1, x2 + half_stroke_width, y1, paint)  # top border
        canvas.drawLine(  # bottom border
            x1 - half_stroke_width, y1 + self.height + self.stroke_width,
            x2 + half_stroke_width, y1 + self.height + self.stroke_width, paint
        )

    def render(self, canvas):
        canvas: skia.Canvas
        # Draw border if it exists
        if self.stroke_width > 0:
            self.render_border(canvas)

        # Draw Fill
        rect = skia.Rect(self.x, self.y, self.x + self.width, self.y + self.height)
        paint = skia.Paint(
            Color=skia.Color(*self.fill),
            Style=skia.Paint.kFill_Style
        )
        # noinspection PyTypeChecker
        canvas.drawRect(rect, paint)
