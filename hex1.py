import arcade
from hexgridcell import HexGridCell
from hexitem import HexItem
from timeit import default_timer as timer

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOARD_WIDTH = 5
BOARD_HEIGHT = 4
CELL_RADIUS = 40

class MyGame(arcade.Window):
    mCells = []

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.mCellMetrics = HexGridCell(CELL_RADIUS)
        self.mcurselrow = -1 # initialization value only
        self.mcurselcol = -1 # initialization value only
        cellrow = []
        for j in range(BOARD_HEIGHT):
            for i in range(BOARD_WIDTH):
                cellrow.append(HexItem(i,j,CELL_RADIUS,HexItem.CELL_UNSELECTED))
            self.mCells.append(cellrow)
            cellrow = []
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def isInsideBoard(self, i, j):
        return i >= 0 and i < BOARD_WIDTH and j >= 0 and j < BOARD_HEIGHT and self.mCells[j][i].getState() != HexItem.CELL_BLANK

    def  toggleCell(self, i, j):
        print(f"toggleCell(): {i} , {j} , {self.mCells[j][i].getState()}")
        print(f"toggleCell(): self.mcurselcol = {self.mcurselcol}, self.mcurselrow = {self.mcurselrow}")

        cell_clicked = self.mCells[j][i]
        old_state = cell_clicked.mState

        # previously highlighted cell clicked
        if i == self.mcurselcol and j == self.mcurselrow:
            print('Case 1')
            if old_state == HexItem.CELL_SELECTED:      # "is" compares two vars to see if they're the same object & can result in weird behavior sometimes
                cell_clicked.mState = HexItem.CELL_UNSELECTED
            elif old_state == HexItem.CELL_UNSELECTED:
                cell_clicked.mState = HexItem.CELL_SELECTED

        # new cell clicked
        if i != self.mcurselcol or j != self.mcurselrow:
            print('Case 2')
            cell_clicked.mState = HexItem.CELL_SELECTED
            if self.mcurselcol >= 0 and self.mcurselrow >= 0:
                self.mCells[self.mcurselrow][self.mcurselcol].mState = HexItem.CELL_UNSELECTED

    #    oldstate = self.mCells[j][i].getState()
    #    if (oldstate is HexItem.CELL_UNSELECTED):
    #        print("toggleCell(): current state is UNSELECTED")

    #    newstate = HexItem.CELL_SELECTED
    #    if (oldstate is HexItem.CELL_SELECTED):
    #        print("toggleCell(): current state is SELECTED")
    #        newstate = HexItem.CELL_UNSELECTED
    #    #self.mCells[j][i].setState(HexItem.CELL_SELECTED if (self.mCells[j][i].getState() == HexItem.CELL_UNSELECTED) else HexItem.CELL_UNSELECTED)
    #    self.mCells[j][i].setState(newstate)
    #    self.mCells[self.mcurselrow][self.mcurselcol].setState(HexItem.CELL_UNSELECTED)
        self.mcurselrow = j
        self.mcurselcol = i

    def on_draw(self):
        start = timer()
        arcade.start_render()
        for j in range(BOARD_HEIGHT):
            for i in range(BOARD_WIDTH):
                if (self.mCells[j][i].getState() != HexItem.CELL_BLANK):
                    color = arcade.color.NAVY_BLUE if (self.mCells[j][i].mState == HexItem.CELL_SELECTED) else arcade.color.GRAY
                    arcade.draw_polygon_filled(self.mCells[j][i].getPointlist(), color)
                    arcade.draw_polygon_outline(self.mCells[j][i].getPointlist(), arcade.color.BLACK)

        end = timer()
        print(f"draw() time: {end - start}")

    def update(self, delta_time):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        clickI, clickJ = self.mCellMetrics.getCellByPoint(x, y)

        if (self.isInsideBoard(clickI, clickJ)):
            # toggle the clicked cell, can't be blank because of isInsideBoard
            self.toggleCell(clickI, clickJ)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Hex Map 1')
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()