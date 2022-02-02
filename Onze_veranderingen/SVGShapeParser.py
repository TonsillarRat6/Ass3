import json
from SVGCircle import SVGCircle
from SVGRectangle import SVGRectangle
from SVGStar import SVGStar
from shape import Shape
from typing import List

class SVGParser:

    def parse_shapes(self, filename: str) -> List[Shape]:
        json_file = open(filename)
        data = json.load(json_file)
        shapes: List[Shape] = []
        for shape_def in data:
            if shape_def["type"] == "circle":
                shapes.append(
                    SVGCircle(shape_def["x"], shape_def["y"], shape_def["radius"], shape_def["color"], shape_def["outline"], shape_def["stroke_thiccness"]))
            elif shape_def["type"] == "rectangle":
                shapes.append(
                    SVGRectangle(shape_def["x"], shape_def["y"], shape_def["width"], shape_def["height"], shape_def["color"], shape_def["outline"], shape_def["stroke_thiccness"]))
            elif shape_def["type"] == "star":
                shapes.append(
                    SVGStar(shape_def["x"], shape_def["y"], shape_def["width"], shape_def["height"], shape_def["pts"], shape_def["color"], shape_def["outline"], shape_def["stroke_thiccness"]))
        return shapes