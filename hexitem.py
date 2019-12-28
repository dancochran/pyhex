import math

class HexItem:
    CELL_BLANK = 0
    CELL_UNSELECTED = 1
    CELL_SELECTED = 84
    NUM_HEX_CORNERS = 6

    def __init__(self, i, j, radius, state):
        self.mRadius = radius
        self.mWidth = radius * 2
        self.mHeight = radius * math.sqrt(3)
        self.mSide = radius * 3 / 2
        self.mCornersDx = []
        self.mCornersDy = []
        self.mCornersX = []
        self.mCornersY = []
        self.mPointlist = []

        self.mCornersDx = [self.mRadius / 2, self.mSide, self.mWidth, self.mSide, self.mRadius / 2, 0 ]
        self.mCornersDy = [0, 0, self.mHeight / 2,self.mHeight, self.mHeight, self.mHeight / 2]
        self.mI = i
        self.mJ = j
        self.mX = i * self.mSide
        self.mY = self.mHeight * (2 * j + (i % 2)) / 2
        for k in range(self.NUM_HEX_CORNERS):
            self.mCornersX.append(self.mX + self.mCornersDx[k])
            self.mCornersY.append(self.mY + self.mCornersDy[k])
            self.mPointlist.append((self.mX + self.mCornersDx[k], self.mY + self.mCornersDy[k]))
        self.mState = state

    def getLeft(self):
        return self.mX

    def getTop(self):
        return self.mY

    def getCenterX(self):
        return self.mX + self.mRadius

    def getCenterY(self):
        return self.mY + self.mHeight / 2
    
    def getIndexI(self):
        return self.mI

    def getIndexJ(self):
        return self.mJ

    def getState(self):
        return self.mState

    def getPointlist(self):
        return self.mPointlist

    def setState(self, state):
        self.mState = state

