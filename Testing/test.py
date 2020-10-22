"""import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

fish_lines = open("DJFishLipsLines.txt")
fish_lines_list = []


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_HEIGHT, SCREEN_WIDTH, "Fish Fight")

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.PALE_PLUM)

    def on_draw(self):
        arcade.start_render()
        for line in fish_lines:
            line = line.strip
            arcade.draw_text(str(line), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.GREEN, 20)
        fish_lines.close()
        arcade.finish_render()


"""

"""def main():
    play_fish_lines.play_fish_lines()


main()
"""

"""


def main():
    # Main method 
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
    """

import arcade

WIDTH = 20
HEIGHT = 20
MARGIN = 5

ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_WIDTH = WIDTH * COLUMN_COUNT + MARGIN * (COLUMN_COUNT + 1)
SCREEN_HEIGHT = HEIGHT * ROW_COUNT + MARGIN * (ROW_COUNT + 1)


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        for i in range(COLUMN_COUNT):
            for j in range(ROW_COUNT):
                arcade.draw_rectangle_filled((MARGIN + WIDTH) * i + MARGIN + WIDTH / 2,
                                             (MARGIN + HEIGHT) * j + MARGIN + HEIGHT / 2,
                                             WIDTH,
                                             HEIGHT,
                                             arcade.color.WHITE)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()