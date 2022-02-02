from numpy import insert
from shape import Shape
from tkinter import Canvas

class Rectangle(Shape):

    def __init__(self, x: int, y: int, width: int, height: int, color: str, outline: str, stroke: str):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.color: str = color
        self.outline: str = outline
        self.stroke: str = stroke
        super().__init__()

    def draw(self, canvas: Canvas):
        canvas.create_rectangle(self.x, 
                                self.y,
                                self.x + self.width,
                                self.y + self.height,
                                fill=self.color,
                                outline=self.outline,
                                width=self.stroke)