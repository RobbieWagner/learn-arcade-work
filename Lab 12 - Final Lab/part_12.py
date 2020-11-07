import arcade
import random
import time

"""
This code is adapted from the Array-Baked Grids lab
"""

# Set how many rows and columns we will have
ROW_COUNT = 3
COLUMN_COUNT = 3

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 100
HEIGHT = 100

BLANK_SPACE = 0

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 20

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + BLANK_SPACE
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN + BLANK_SPACE


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)

        self.clicks = 0
        self.required_clicks = 1
        self.row_clicked = 0
        self.column_clicked = 0
        self.return_value = 0
        self.grid = []

        # initialization of the board
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(10)

        # gives each box a unique color
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                checking = True
                some_value = 0

                # picks a color, and assigns it if it is unique
                while checking:
                    color_value = random.randrange(9)
                    print("color", color_value)
                    for checking_row in range(ROW_COUNT):
                        for checking_column in range(COLUMN_COUNT):
                            if self.grid[checking_row][checking_column] != color_value:
                                some_value += 1
                                print(some_value)
                            if some_value == COLUMN_COUNT * ROW_COUNT:
                                print("color", color_value)
                                checking = False
                            elif checking_row == ROW_COUNT - 1 and checking_column == COLUMN_COUNT - 1:
                                some_value = 0

                self.grid[row][column] = color_value

        arcade.set_background_color(arcade.color.BLACK)

        """ Create a list to hold buffered shapes, and load the list """
        self.grid_shape_list = None
        self.create_shapes_from_grid()

    def on_update(self, delta_time: float):
        if self.grid[0][0] == 10:
            time.sleep(.5)

            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    checking = True
                    some_value = 0

                    # picks a color, and assigns it if it is unique
                    while checking:
                        color_value = random.randrange(9)
                        print("color", color_value)
                        for checking_row in range(ROW_COUNT):
                            for checking_column in range(COLUMN_COUNT):
                                if self.grid[checking_row][checking_column] != color_value:
                                    some_value += 1
                                    print(some_value)
                                if some_value == COLUMN_COUNT * ROW_COUNT:
                                    print("color", color_value)
                                    checking = False
                                elif checking_row == ROW_COUNT - 1 and checking_column == COLUMN_COUNT - 1:
                                    some_value = 0

                    self.grid[row][column] = color_value

            self.create_shapes_from_grid()

    def create_shapes_from_grid(self):
        self.grid_shape_list = arcade.ShapeElementList()

        # makes each box
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                # Figure out what color to draw the box
                if self.grid[row][column] == 0:
                    color = arcade.color.SALMON
                elif self.grid[row][column] == 1:
                    color = arcade.color.GRAY
                elif self.grid[row][column] == 2:
                    color = arcade.color.BLUE
                elif self.grid[row][column] == 3:
                    color = arcade.color.YELLOW
                elif self.grid[row][column] == 4:
                    color = arcade.color.PURPLE
                elif self.grid[row][column] == 5:
                    color = arcade.color.ORANGE
                elif self.grid[row][column] == 6:
                    color = arcade.color.AMAZON
                elif self.grid[row][column] == 7:
                    color = arcade.color.OLIVE
                elif self.grid[row][column] == 8:
                    color = arcade.color.AQUA
                elif self.grid[row][column] == 9:
                    color = arcade.color.GREEN
                elif self.grid[row][column] == 10:
                    color = arcade.color.WHITE

                # Figure where to put the box
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Create the box and add to the list
                rectangle = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, color)
                self.grid_shape_list.append(rectangle)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        arcade.start_render()

        self.grid_shape_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        # Change the x/y screen coordinates to grid coordinates
        self.column_clicked = int(x // (WIDTH + MARGIN))
        self.row_clicked = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({self.row_clicked}, {self.column_clicked})")

        # this assures that nothing happens unless they click somewhere on the grid
        if self.row_clicked < ROW_COUNT and self.column_clicked < COLUMN_COUNT:

            # Highlight the box they clicked
            self.return_value = self.grid[self.row_clicked][self.column_clicked]
            self.grid[self.row_clicked][self.column_clicked] = 9

            # checks if they finished the level
            self.clicks += 1

        self.create_shapes_from_grid()

    def on_mouse_release(self, x, y, button, modifiers):

        print(f"Release coordinates: ({self.row_clicked}, {self.column_clicked})")

        if self.row_clicked < ROW_COUNT and self.column_clicked < COLUMN_COUNT:

            self.grid[self.row_clicked][self.column_clicked] = self.return_value

            # turns the grid to white and
            if self.clicks == self.required_clicks:
                for row in range(ROW_COUNT):
                    for column in range(COLUMN_COUNT):
                        self.grid[row][column] = 10
                self.clicks = 0
                self.required_clicks += 1

        self.create_shapes_from_grid()


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
