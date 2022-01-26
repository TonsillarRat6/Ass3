from shape import Shape
import math
from tkinter import Canvas

class Star(Shape):

    def __init__(self, x: int, y: int, width: int, height: int, color: str, outline: str):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.color: str = color
        self.outline: str = outline
        super().__init__()

    def get_pts_list(self):
        numPoints = 3
        pts = []
        rx = self.width / 2 
        ry = self.height / 2 
        cx = self.x + rx 
        cy = self.y + ry 
        theta = -math.pi / 2 
        dtheta = 4 * math.pi / numPoints

        for i in range(0, numPoints + 1):
            pts.append(
                int(round(cx + rx * math.cos(theta)))) #
            pts.append(
                int(round(cy + ry * math.sin(theta)))
            )
            theta += dtheta
        return pts

    def adapt_pts(self):
        temp = iter(self.get_pts_list())
        return zip(temp, temp)

    def draw(self, canvas: Canvas):
        # we use the '*' syntax here to convert the list of points to function arguments
        canvas.create_polygon(*self.get_pts_list(), fill=self.color, outline=self.outline)


    def drawSVG(self, svgFile):
        svgFile.add(svgFile.polygon(
            points=self.adapt_pts(),
            fill=self.color,
            stroke=self.outline
        ))
