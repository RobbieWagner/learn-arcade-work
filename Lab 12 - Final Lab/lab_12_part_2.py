"""
Color Switch Simon
This code is adapted from the Array-Backed Grids lab
"""

import arcade
import switch_it_up
import random


# Set how many rows and columns we will have
ROW_COUNT = 3
COLUMN_COUNT = 3

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 100
HEIGHT = 100

BLANK_SPACE = 50

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 20

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN + BLANK_SPACE

# sounds from kenney.nl
BUTTON_SOUND = arcade.load_sound("impactMetal_003.ogg")
RESET_SOUND = arcade.load_sound("forceField_003.ogg")
BAD_CLICK_SOUND = arcade.load_sound("laserRetro_001.ogg")


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)

        self.grid = []

        self.clicks = 0
        self.required_clicks = 1
        self.goal_tracker = 0
        self.row_clicked = 0
        self.column_clicked = 0
        self.clicker_array = []

        self.score = 0

        self.return_value = 0

        self.countdown = 0

        self.all_flashed = False
        self.flash_count = 0
        self.flash_array = []
        self.flash_requirement = 1
        self.flashing = False
        self.dummy_array1 = []
        self.dummy_array2 = []

        self.started = False

        switch_it_up.reset_the_board(self.grid, ROW_COUNT, COLUMN_COUNT, self.flash_array, self.clicker_array)
        self.board_reset = True

        arcade.set_background_color(arcade.color.BLACK)

        """ Create a list to hold buffered shapes, and load the list """
        self.grid_shape_list = None
        self.create_shapes_from_grid()

    def on_update(self, delta_time):
        if self.started:

            if self.countdown:
                self.countdown -= 1

            if self.all_flashed and self.board_reset and self.countdown == 1:
                self.board_reset = False
                switch_it_up.reset_the_board(self.grid, ROW_COUNT, COLUMN_COUNT, self.dummy_array1, self.dummy_array2)

                self.countdown = 30
                self.create_shapes_from_grid()

            if self.grid[0][0] == 10 and self.countdown == 0:

                switch_it_up.reset_the_board(self.grid, ROW_COUNT, COLUMN_COUNT, self.flash_array, self.clicker_array)
                self.board_reset = True
                self.score += 1
                self.all_flashed = False

                # sound from kenney.nl
                arcade.play_sound(RESET_SOUND)

                self.countdown = 30
                self.create_shapes_from_grid()

                # checks to see if lights still need to flash
            elif self.countdown == 0 and self.all_flashed == False and self.board_reset:
                flash_value = random.randrange(9)
                self.flash_array.append(flash_value)
                self.flash_count += 1
                self.countdown = 30

                # finds which color to flash and flashes it
                for row in range(ROW_COUNT):
                    for column in range(COLUMN_COUNT):
                        if flash_value == self.grid[row][column]:
                            self.return_value = self.grid[row][column]
                            self.grid[row][column] = 9
                            self.flashing = True

                # checks to see if all the squares that needed to flash did
                if self.flash_count == self.flash_requirement:
                    self.flash_count = 0
                    self.flash_requirement += 1
                    self.all_flashed = True
                    self.countdown = 30

                # need to reset countdown everytime

                self.create_shapes_from_grid()

            if self.flashing and self.countdown == 3:
                for row in range(ROW_COUNT):
                    for column in range(COLUMN_COUNT):
                        if self.grid[row][column] == 9:
                            self.grid[row][column] = self.return_value
                self.flashing = False
                self.countdown = 30
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
                else:
                    color = arcade.color.RED

                # Figure where to put the box
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Create the box and add to the list
                rectangle = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, color)
                self.grid_shape_list.append(rectangle)

    def on_draw(self):
        if self.started:
            """ Render the screen. """

            # This command has to happen before we start drawing
            arcade.start_render()

            self.grid_shape_list.draw()

            arcade.draw_text(f"Score: {self.score}",
                             MARGIN,
                             (HEIGHT + MARGIN) * ROW_COUNT + BLANK_SPACE / 2,
                             arcade.color.WHITE)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.started:
            """ Called when the user presses a mouse button. """
            # Change the x/y screen coordinates to grid coordinates
            self.column_clicked = int(x // (WIDTH + MARGIN))
            self.row_clicked = int(y // (HEIGHT + MARGIN))

            # this assures that nothing happens unless they click somewhere on the grid
            if self.row_clicked < ROW_COUNT \
                    and self.column_clicked < COLUMN_COUNT \
                    and self.grid[self.row_clicked][self.column_clicked] < 10 \
                    and self.all_flashed:

                self.clicker_array.append(self.grid[self.row_clicked][self.column_clicked])

                # Highlight the box they clicked
                self.return_value = self.grid[self.row_clicked][self.column_clicked]
                self.grid[self.row_clicked][self.column_clicked] = 9

                # checks if they finished the level
                self.clicks += 1
                arcade.play_sound(BUTTON_SOUND)
            else:
                arcade.play_sound(BAD_CLICK_SOUND)

            # sound from kenney.nl
            self.create_shapes_from_grid()

    def on_mouse_release(self, x, y, button, modifiers):
        if self.started:
            if self.row_clicked < ROW_COUNT \
                    and self.column_clicked < COLUMN_COUNT \
                    and self.grid[self.row_clicked][self.column_clicked] == 9:

                self.grid[self.row_clicked][self.column_clicked] = self.return_value

                # turns the grid to white and
                if self.clicks == self.required_clicks:
                    for i in range(self.clicks):
                        if self.flash_array[i] == self.clicker_array[i]:
                            self.goal_tracker += 1
                    if self.goal_tracker == self.required_clicks:
                        for row in range(ROW_COUNT):
                            for column in range(COLUMN_COUNT):
                                self.grid[row][column] = 10
                        self.countdown = 30
                        self.clicks = 0
                        self.required_clicks += 1
                        self.goal_tracker = 0
                    else:
                        for row in range(ROW_COUNT):
                            for column in range(COLUMN_COUNT):
                                self.grid[row][column] = 11

            self.create_shapes_from_grid()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.started = True
            self.countdown = 30


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
