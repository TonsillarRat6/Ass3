from star import Star


class SVGStar(Star):

    def adapt_pts(self):
        temp = iter(self.get_pts_list())
        return zip(temp, temp)

    def draw(self, svgFile):
        svgFile.add(svgFile.polygon(
            points=self.adapt_pts(),
            fill=self.color,
            stroke=self.outline,
            stroke_width=self.stroke
        ))