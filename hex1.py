import arcade
from hexgridcell import HexGridCell

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOARD_WIDTH = 5
BOARD_HEIGHT = 4
CELL_BLANK = 0
CELL_UNSELECTED = 1
CELL_SELECTED = 84
NUM_HEX_CORNERS = 6
CELL_RADIUS = 40

class MyGame(arcade.Window):
    mCells = [
        [CELL_UNSELECTED, CELL_UNSELECTED, CELL_UNSELECTED, CELL_UNSELECTED, CELL_UNSELECTED],
        [CELL_UNSELECTED, CELL_UNSELECTED, CELL_UNSELECTED, CELL_UNSELECTED, CELL_UNSELECTED],
        [CELL_UNSELECTED, CELL_UNSELECTED, CELL_BLANK, CELL_UNSELECTED, CELL_UNSELECTED],
        [CELL_UNSELECTED, CELL_UNSELECTED, CELL_UNSELECTED, CELL_UNSELECTED, CELL_UNSELECTED]
    ]

    mCornersX = []
    mCornersY = []

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.mCellMetrics = HexGridCell(CELL_RADIUS)
        self.mcurselrow = 0
        self.mcurselcol = 0
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def isInsideBoard(self, i, j):
        return i >= 0 and i < BOARD_WIDTH and j >= 0 and j < BOARD_HEIGHT and self.mCells[j][i] != CELL_BLANK

    def  toggleCell(self, i, j):
        self.mCells[self.mcurselrow][self.mcurselcol] = CELL_UNSELECTED 
        self.mCells[j][i] = CELL_SELECTED if (self.mCells[j][i] == CELL_UNSELECTED) else CELL_UNSELECTED
        self.mcurselrow = j
        self.mcurselcol = i

    def on_draw(self):
        #print(f"on_draw(): entering, BOARD_HEIGHT = {BOARD_HEIGHT}")
        arcade.start_render()
        tothex = 0
        for j in range(BOARD_HEIGHT):
            #print(f"height iteration: {j}")
            for i in range(BOARD_WIDTH):
                #print(f"width iteration: {i}")
                self.mCellMetrics.setCellIndex(i, j)
                if (self.mCells[j][i] != CELL_BLANK):
                    tothex += 1
                    self.mCellMetrics.computeCorners(self.mCornersX, self.mCornersY)
                    #print(f"called computeCorners: {i}")
                    #color = arcade.color.NAVY_BLUE if (self.mCells[j][i] == CELL_SELECTED) else arcade.color.GRAY
                    color = arcade.color.NAVY_BLUE if (self.mCells[j][i] == CELL_SELECTED) else arcade.color.GRAY
                    pointlist = []
                    for k in range(NUM_HEX_CORNERS):
                        #print(f"corners iteration: {k}")
                        pointlist.append((self.mCornersX[k], self.mCornersY[k]))
                    #print(pointlist)
                    arcade.draw_polygon_filled(pointlist, color)
                    arcade.draw_polygon_outline(pointlist, arcade.color.BLACK)

                self.mCornersX.clear()
                self.mCornersY.clear()

        #print(f"tothex: {tothex}")

    def update(self, delta_time):
        pass

    #def on_mouse_motion(self, x, y, dx, dy):

    #def on_mouse_press(self, x, y, button, modifiers):
        #print(f"clicked button number: {button}")
        #if button == arcade.MOUSE_BUTTON_LEFT:

    def on_mouse_release(self, x, y, button, modifiers):
        #print(f"released button number: {button}")
        #if button == arcade.MOUSE_BUTTON_LEFT:
        self.mCellMetrics.setCellByPoint(x, y)
        clickI = self.mCellMetrics.getIndexI()
        clickJ = self.mCellMetrics.getIndexJ()

        if (self.isInsideBoard(clickI, clickJ)):
            # toggle the clicked cell, can't be blank because of isInsideBoard
            self.toggleCell(clickI, clickJ)

    #def on_key_press(self, key, modifiers):
        #print(f"pressed key: {key}")
        #if key == arcade.key.LEFT:
        #elif key == arcade.key.RIGHT:
        #elif key == arcade.key.UP:
        #elif key == arcade.key.DOWN:

    #def on_key_release(self, key, modifiers):
        #print(f"released key: {key}")
        #if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        #elif key == arcade.key.UP or key == arcade.key.DOWN:

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Hex Map 1')
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()