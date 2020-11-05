import arcade
import random

"""
This code is adapted from the Array-Baked Grids lab
"""

# Set how many rows and columns we will have
ROW_COUNT = 20
COLUMN_COUNT = 40

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

BLANK_SPACE = 0

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 12

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

        self.mouse_pressed = False
        self.row_clicked = 0
        self.column_clicked = 0
        self.grid = []

        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        for i in range(random.randrange(5)):
            self.grid[random.randrange(ROW_COUNT)][random.randrange(COLUMN_COUNT)] = 4

        arcade.set_background_color(arcade.color.BLACK)

        """ Create a list to hold buffered shapes, and load the list """
        self.grid_shape_list = None
        self.create_shapes_from_grid()

    def create_shapes_from_grid(self):
        """ This creates a list of buffered shapes, and loads the
        rectangles into that list for faster display. """
        self.grid_shape_list = arcade.ShapeElementList()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                # Figure out what color to draw the box
                if self.grid[row][column] == 2:
                    color = arcade.color.WHITE
                elif self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                elif self.grid[row][column] == 0:
                    color = (random.randrange(70), random.randrange(70), random.randrange(70))
                elif self.grid[row][column] == 3:
                    color = arcade.color.GRAY
                elif self.grid[row][column] == 4:
                    color = (random.randrange(100, 200), random.randrange(100, 200), random.randrange(100, 200))

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
        self.mouse_pressed = True
        # Change the x/y screen coordinates to grid coordinates
        self.column_clicked = int(x // (WIDTH + MARGIN))
        self.row_clicked = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({self.row_clicked}, {self.column_clicked})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if self.row_clicked < ROW_COUNT and self.column_clicked < COLUMN_COUNT:

            # Highlight center
            if self.grid[self.row_clicked][self.column_clicked] == 0 \
                    or self.grid[self.row_clicked][self.column_clicked] == 4:
                self.grid[self.row_clicked][self.column_clicked] = 1
            elif self.grid[self.row_clicked][self.column_clicked] == 2:
                self.grid[self.row_clicked][self.column_clicked] = 3

            # Highlight bottom left
            if self.row_clicked > 0 \
                    and self.column_clicked > 0 \
                    and (self.grid[self.row_clicked - 1][self.column_clicked - 1] == 0
                         or self.grid[self.row_clicked - 1][self.column_clicked - 1] == 4):
                self.grid[self.row_clicked - 1][self.column_clicked - 1] = 1
            elif self.row_clicked > 0 \
                    and self.column_clicked > 0 \
                    and self.grid[self.row_clicked - 1][self.column_clicked - 1] == 2:
                self.grid[self.row_clicked - 1][self.column_clicked - 1] = 3

            # Highlight bottom middle
            if self.row_clicked > 0 \
                    and (self.grid[self.row_clicked-1][self.column_clicked] == 0
                         or self.grid[self.row_clicked - 1][self.column_clicked] == 4):
                self.grid[self.row_clicked-1][self.column_clicked] = 1
            elif self.row_clicked > 0 \
                    and self.grid[self.row_clicked-1][self.column_clicked] == 2:
                self.grid[self.row_clicked-1][self.column_clicked] = 3

            # Highlight bottom right
            if self.row_clicked > 0 \
                    and self.column_clicked < COLUMN_COUNT - 1 \
                    and (self.grid[self.row_clicked - 1][self.column_clicked + 1] == 0
                         or self.grid[self.row_clicked - 1][self.column_clicked + 1] == 4):
                self.grid[self.row_clicked - 1][self.column_clicked + 1] = 1
            elif self.row_clicked > 0 \
                    and self.column_clicked < COLUMN_COUNT - 1 \
                    and self.grid[self.row_clicked - 1][self.column_clicked + 1] == 2:
                self.grid[self.row_clicked - 1][self.column_clicked + 1] = 3

            # Highlight center right
            if self.column_clicked < COLUMN_COUNT - 1 \
                    and (self.grid[self.row_clicked][self.column_clicked + 1] == 0
                         or self.grid[self.row_clicked][self.column_clicked + 1] == 4):
                self.grid[self.row_clicked][self.column_clicked + 1] = 1
            elif self.column_clicked < COLUMN_COUNT - 1 \
                    and self.grid[self.row_clicked][self.column_clicked + 1] == 2:
                self.grid[self.row_clicked][self.column_clicked + 1] = 3

            # Highlight center left
            if self.column_clicked > 0 \
                    and (self.grid[self.row_clicked][self.column_clicked - 1] == 0
                         or self.grid[self.row_clicked][self.column_clicked - 1] == 4):
                self.grid[self.row_clicked][self.column_clicked - 1] = 1
            elif self.column_clicked > 0 \
                    and self.grid[self.row_clicked][self.column_clicked - 1] == 2:
                self.grid[self.row_clicked][self.column_clicked - 1] = 3

            # Highlight top left
            if self.row_clicked < ROW_COUNT - 1 \
                    and self.column_clicked > 0 \
                    and (self.grid[self.row_clicked + 1][self.column_clicked - 1] == 0
                         or self.grid[self.row_clicked + 1][self.column_clicked - 1] == 4):
                self.grid[self.row_clicked + 1][self.column_clicked - 1] = 1
            elif self.row_clicked < ROW_COUNT - 1 \
                    and self.column_clicked > 0 \
                    and self.grid[self.row_clicked + 1][self.column_clicked - 1] == 2:
                self.grid[self.row_clicked + 1][self.column_clicked - 1] = 3

            # Highlight top middle
            if self.row_clicked < ROW_COUNT - 1 \
                    and (self.grid[self.row_clicked + 1][self.column_clicked] == 0
                         or self.grid[self.row_clicked + 1][self.column_clicked] == 4):
                self.grid[self.row_clicked + 1][self.column_clicked] = 1
            elif self.row_clicked < ROW_COUNT - 1 \
                    and self.grid[self.row_clicked + 1][self.column_clicked] == 2:
                self.grid[self.row_clicked + 1][self.column_clicked] = 3

            # Highlight top right
            if self.row_clicked < ROW_COUNT - 1 \
                    and self.column_clicked < COLUMN_COUNT - 1 \
                    and (self.grid[self.row_clicked + 1][self.column_clicked + 1] == 0
                         or self.grid[self.row_clicked + 1][self.column_clicked + 1] == 4):
                self.grid[self.row_clicked + 1][self.column_clicked + 1] = 1
            elif self.row_clicked < ROW_COUNT - 1 \
                    and self.column_clicked < COLUMN_COUNT - 1 \
                    and self.grid[self.row_clicked + 1][self.column_clicked + 1] == 2:
                self.grid[self.row_clicked + 1][self.column_clicked + 1] = 3

        self.create_shapes_from_grid()

    def on_mouse_release(self, x, y, button, modifiers):

        self.mouse_pressed = False

        print(f"Release coordinates: ({self.row_clicked}, {self.column_clicked})")

        if self.row_clicked < ROW_COUNT and self.column_clicked < COLUMN_COUNT:

            # Flip center
            if self.grid[self.row_clicked][self.column_clicked] == 1:
                self.grid[self.row_clicked][self.column_clicked] = 2
            elif self.grid[self.row_clicked][self.column_clicked] == 3:
                self.grid[self.row_clicked][self.column_clicked] = 0

            # Flip bottom left
            if self.row_clicked > 0 and self.column_clicked > 0 \
                    and self.grid[self.row_clicked-1][self.column_clicked-1] == 1:
                self.grid[self.row_clicked-1][self.column_clicked-1] = 2
            elif self.row_clicked > 0 and self.column_clicked > 0 \
                    and self.grid[self.row_clicked-1][self.column_clicked-1] == 3:
                self.grid[self.row_clicked - 1][self.column_clicked - 1] = 0

            # Flip bottom middle
            if self.row_clicked > 0 and self.grid[self.row_clicked - 1][self.column_clicked] == 1:
                self.grid[self.row_clicked - 1][self.column_clicked] = 2
            elif self.row_clicked > 0 and self.grid[self.row_clicked - 1][self.column_clicked] == 3:
                self.grid[self.row_clicked - 1][self.column_clicked] = 0

            # Flip bottom right
            if self.row_clicked > 0 and self.column_clicked < COLUMN_COUNT - 1 \
                    and self.grid[self.row_clicked - 1][self.column_clicked + 1] == 1:
                self.grid[self.row_clicked - 1][self.column_clicked + 1] = 2
            elif self.row_clicked > 0 and self.column_clicked < COLUMN_COUNT - 1 \
                    and self.grid[self.row_clicked - 1][self.column_clicked + 1] == 3:
                self.grid[self.row_clicked - 1][self.column_clicked + 1] = 0

            # Flip center right
            if self.column_clicked < COLUMN_COUNT - 1 and self.grid[self.row_clicked][self.column_clicked + 1] == 1:
                self.grid[self.row_clicked][self.column_clicked + 1] = 2
            elif self.column_clicked < COLUMN_COUNT - 1 and self.grid[self.row_clicked][self.column_clicked + 1] == 3:
                self.grid[self.row_clicked][self.column_clicked + 1] = 0

            # Flip center left
            if self.column_clicked > 0 and self.grid[self.row_clicked][self.column_clicked - 1] == 1:
                self.grid[self.row_clicked][self.column_clicked - 1] = 2
            elif self.column_clicked > 0 and self.grid[self.row_clicked][self.column_clicked - 1] == 3:
                self.grid[self.row_clicked][self.column_clicked - 1] = 0

            # Flip top left
            if self.row_clicked < ROW_COUNT - 1 and self.column_clicked > 0 \
                    and self.grid[self.row_clicked + 1][self.column_clicked - 1] == 1:
                self.grid[self.row_clicked + 1][self.column_clicked - 1] = 2
            elif self.row_clicked < ROW_COUNT - 1 and self.column_clicked > 0 \
                    and self.grid[self.row_clicked + 1][self.column_clicked - 1] == 3:
                self.grid[self.row_clicked + 1][self.column_clicked - 1] = 0

            # Flip top middle
            if self.row_clicked < ROW_COUNT - 1 and self.grid[self.row_clicked + 1][self.column_clicked] == 1:
                self.grid[self.row_clicked + 1][self.column_clicked] = 2
            elif self.row_clicked < ROW_COUNT - 1 and self.grid[self.row_clicked + 1][self.column_clicked] == 3:
                self.grid[self.row_clicked + 1][self.column_clicked] = 0

            # Flip top right
            if self.row_clicked < ROW_COUNT - 1 and self.column_clicked < COLUMN_COUNT - 1 \
                    and self.grid[self.row_clicked + 1][self.column_clicked + 1] == 1:
                self.grid[self.row_clicked + 1][self.column_clicked + 1] = 2
            elif self.row_clicked < ROW_COUNT - 1 and self.column_clicked < COLUMN_COUNT - 1 \
                    and self.grid[self.row_clicked + 1][self.column_clicked + 1] == 3:
                self.grid[self.row_clicked + 1][self.column_clicked + 1] = 0

        self.create_shapes_from_grid()


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
