from circle import Circle


class SVGCircle(Circle):

    def draw(self, svgFile):
        svgFile.add(svgFile.circle(
            center = (self.x, self.y),
            r = self.radius,
            fill=self.color,
            stroke=self.outline,
            stroke_width=self.stroke
        ))