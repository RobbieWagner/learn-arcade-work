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


