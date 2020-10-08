# All sprites and sounds used were found and can be found on Kenny.nl

import arcade
import random

# Initialize all of the universal variables here
SPRITE_SCALING_PLAYER = .75
SPRITE_SCALING_GEM = 1
SPRITE_SCALING_HAZARD = .5
GEM_COUNT = 50
HAZARD_COUNT = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Sounds from Kenny.nl
bad_sound = arcade.load_sound("impactTin_medium_000.ogg")
good_sound = arcade.load_sound("impactMining_003.ogg")


class Gem(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        # See if we went off-screen
        if self.center_y < -20:
            self.center_y = SCREEN_HEIGHT + 20


class Hazard(arcade.Sprite):

    def update(self):
        self.center_x -= 1

        if self.center_x < -20:
            self.center_x = SCREEN_WIDTH + 20


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Robbie's Amazing Fantastic Super Cool Sprite Lab Submission")

        # Variables that will hold sprite lists
        self.player_list = None
        self.gem_list = None
        self.hazard_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.PINK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.hazard_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # The player score
        self.score = 0

        # Set up the player (image from Kenny.nl)
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the gems
        for i in range(GEM_COUNT):

            # Create the gem instance (image from Kenny.nl)
            gem = Gem("gem.png", SPRITE_SCALING_GEM)

            # Position the gem
            gem.center_x = random.randrange(SCREEN_WIDTH)
            gem.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the gem to the list
            self.gem_list.append(gem)

        for i in range(HAZARD_COUNT):

            # Create the hazard instance (image from Kenny.nl)
            hazard = Hazard("hazard.png", SPRITE_SCALING_HAZARD)

            # Position the hazard
            hazard.center_x = random.randrange(SCREEN_WIDTH)
            hazard.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the hazard to the lists
            self.hazard_list.append(hazard)

    def on_draw(self):
        """ Draw the game objects """
        arcade.start_render()
        self.gem_list.draw()
        self.player_list.draw()
        self.hazard_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.gem_list) == 0:
            arcade.draw_text("Game Over", SCREEN_WIDTH/2-70, SCREEN_HEIGHT/2-20, arcade.color.SMOKY_BLACK, 25)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Mouse Controls """

        if len(self.gem_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ For the movement of sprites and score """
        if len(self.gem_list) > 0:
            self.gem_list.update()
            self.hazard_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.gem_list)
        hit_list_hazard = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.hazard_list)
        for gem in hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(good_sound, 5)
        for hazard in hit_list_hazard:
            hazard.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(bad_sound, 5)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
