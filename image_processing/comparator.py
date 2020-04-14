from PIL import Image, ImageChops
from typing import List
from data_struct.rgba_rect import RGBARect
from image_processing.creator import createImage
import numpy


class Comparator:

    def __init__(self, imagePath: str):
        self.refImage = Image.open(imagePath)

    def evaluate(self, individual: List[RGBARect]) -> float:
        image = createImage(
            individual, self.refImage.size[0], self.refImage.size[1])
        diffImage = ImageChops.difference(self.refImage.convert('RGBA'), image)
        return 1 - self.__calculate(diffImage)

    def __calculate(self, diffImage: Image) -> float:
        pixelsNo = diffImage.size[0] * diffImage.size[1]
        diff = numpy.sum(diffImage) / float(4 * pixelsNo)
        return diff / 255.0
