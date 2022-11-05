import skia


class Line:
    def __init__(self, x1, y1, x2, y2, width=2, fill=(255, 86, 128, 255)):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.width = width
        self.fill = fill

    def render(self, canvas):
        canvas: skia.Canvas
        canvas.drawLine(
            self.x1, self.y1, self.x2, self.y2,
            skia.Paint(
                Color=skia.Color(*self.fill),
                StrokeWidth=self.width,
                StrokeCap=skia.Paint.kRound_Cap,
            )
        )


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
        half_stroke_width = self.stroke_width / 2
        paint = skia.Paint(StrokeWidth=self.stroke_width, Color=skia.Color(*self.stroke_color),
                           Style=skia.Paint.kStroke_Style)
        rect = skia.Rect(
            self.x - half_stroke_width, self.y - half_stroke_width,
            self.x + self.width + half_stroke_width, self.y + self.height + half_stroke_width
        )
        # noinspection PyTypeChecker
        canvas.drawRect(rect, paint)

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


class Circle:
    def __init__(self, x, y, radius, stroke_width=20, stroke_color=(255, 86, 128, 255),
                 fill=(199, 199, 199, 255)):
        self.x, self.y = x, y
        self.radius = radius
        self.stroke_width = stroke_width
        self.stroke_color = stroke_color
        self.fill = fill

    def render_border(self, canvas):
        canvas: skia.Canvas
        half_stroke_width = self.stroke_width / 2
        paint = skia.Paint(StrokeWidth=self.stroke_width, Color=skia.Color(*self.stroke_color),
                           Style=skia.Paint.kStroke_Style)
        canvas.drawCircle(self.x, self.y, self.radius + half_stroke_width, paint)

    def render(self, canvas):
        canvas: skia.Canvas
        # Draw border if it exists
        if self.stroke_width > 0:
            self.render_border(canvas)

        # Draw Fill
        paint = skia.Paint(Color=skia.Color(*self.fill), Style=skia.Paint.kFill_Style)
        canvas.drawCircle(self.x, self.y, self.radius, paint)
