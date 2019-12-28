import math

class HexGridCell:
    NEIGHBORS_DI = [0, 1, 1, 0, -1, -1]
    NEIGHBORS_DJ = [[-1, -1, 0, 1, 0, -1 ], [-1, 0, 1, 1, 1, 0]]
    SIDE = 0
    RADIUS = 0
    HEIGHT = 0
    WIDTH = 0
    NUM_NEIGHBORS = 6

    def __init__(self, radius):
        self.RADIUS = radius
        self.WIDTH = radius * 2
        self.HEIGHT = radius * math.sqrt(3)
        self.SIDE = radius * 3 / 2

    def getCellByPoint(self, x, y):
        ci = math.floor(x/self.SIDE)
        cx = x - self.SIDE*ci

        ty = y - (ci % 2) * self.HEIGHT / 2
        cj = math.floor(ty / self.HEIGHT)
        cy = ty - self.HEIGHT * cj
        
        if (cx > abs(self.RADIUS / 2 - self.RADIUS * cy / self.HEIGHT)):
            return (ci, cj)
        else:
            return (ci - 1, cj + (ci % 2) - (1 if (cy < self.HEIGHT / 2) else 0))
