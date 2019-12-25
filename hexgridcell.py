import math

class HexGridCell:
    NEIGHBORS_DI = [0, 1, 1, 0, -1, -1]
    NEIGHBORS_DJ = [[-1, -1, 0, 1, 0, -1 ], [-1, 0, 1, 1, 1, 0]]
    CORNERS_DX = []
    CORNERS_DY = []
    SIDE = 0
    mX = 0
    mY = 0
    mI = 0
    mJ = 0
    RADIUS = 0
    HEIGHT = 0
    WIDTH = 0
    NUM_NEIGHBORS = 6

    def __init__(self, radius):
        self.RADIUS = radius
        self.WIDTH = radius * 2
        self.HEIGHT = radius * math.sqrt(3)
        self.SIDE = radius * 3 / 2
        self.CORNERS_DX = [self.RADIUS / 2, self.SIDE, self.WIDTH, self.SIDE, self.RADIUS / 2, 0 ]
        self.CORNERS_DY = [0, 0, self.HEIGHT / 2,self.HEIGHT, self.HEIGHT, self.HEIGHT / 2]

    def getLeft(self):
        return self.mX

    def getTop(self):
        return self.mY

    def getCenterX(self):
        return self.mX + self.RADIUS

    def getCenterY(self):
        return self.mY + self.HEIGHT / 2
    
    def getIndexI(self):
        return self.mI

    def getIndexJ(self):
        return self.mJ

    def getNeighborI(self, neighborIdx):
        return self.mI + self.NEIGHBORS_DI[neighborIdx]

    def getNeighborJ(self, neighborIdx):
        return self.mJ + self.NEIGHBORS_DJ[self.mI % 2][neighborIdx]

    def computeCorners(self, cornersX = [], cornersY = []):
        #print(f"computeCorners:: mX: {self.mX} , mY: {self.mY}")
        for k in range(self.NUM_NEIGHBORS):
            #print(f"computeCorners::neighbor iteration: {k}")
            #cornersX.append(84)
            #print("computeCorners::set individual element")
            cornersX.append(self.mX + self.CORNERS_DX[k])
            #print(f"computeCorners::result: {self.mX + self.CORNERS_DX[k]}")
            #print(f"computeCorners::cornersX[k] = : {cornersX[k]}")
            cornersY.append(self.mY + self.CORNERS_DY[k])

    def setCellIndex(self, i, j):
        self.mI = i
        self.mJ = j
        self.mX = i * self.SIDE
        self.mY = self.HEIGHT * (2 * j + (i % 2)) / 2

    def setCellByPoint(self, x, y):
        ci = math.floor(x/self.SIDE)
        cx = x - self.SIDE*ci

        ty = y - (ci % 2) * self.HEIGHT / 2
        cj = math.floor(ty / self.HEIGHT)
        cy = ty - self.HEIGHT * cj
        
        if (cx > abs(self.RADIUS / 2 - self.RADIUS * cy / self.HEIGHT)):
            self.setCellIndex(ci, cj)
        else:
            self.setCellIndex(ci - 1, cj + (ci % 2) - (1 if (cy < self.HEIGHT / 2) else 0))
