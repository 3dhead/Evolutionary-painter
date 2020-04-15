from data_struct.rgba_rect import RGBARect
from random import seed
from random import randint
from typing import List

class Individual:
    def __init__(self, offspringRects = None, offspringDeviations = None ):
        if offspringRects == None :
            self.rects = list()
        else:
            self.rects = offspringRects
        if offspringDeviations == None :
            self.deviations = list()
        else:
            self.deviations = offspringDeviations

    def cross(self, individual):
        rects = list()
        deviations = list()
        for i in range(0, len(self.rects)):
            rects.append((self.rects[i]+individual.rects[i])//2)
            deviations.append(self.deviations[i]+individual.deviations[i]//2)
        return Individual(rects, deviations)