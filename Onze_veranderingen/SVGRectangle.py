from rectangle import Rectangle


class SVGRectangle(Rectangle):

    def draw(self, svgFile):
        svgFile.add(svgFile.rect(
            insert = (self.x, self.y),
            size = (self.width, self.height),
            fill=self.color,
            stroke=self.outline,
            stroke_width=self.stroke
        ))