""" Sprite Sample Program """

import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 2
SPRITE_SCALING_PLAYER = 4

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

MOVEMENT_SPEED = 5

VIEWPORT_MARGIN = SCREEN_HEIGHT/2


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.hazard_list = None

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        self.view_left = 0
        self.view_bottom = 0

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        self.view_left = 0
        self.view_bottom = 0

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.hazard_list = arcade.SpriteList()

        # Create the player
        self.player_sprite = arcade.Sprite("../Lab 09 - Sprites and Walls/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # --- Place boxes inside a loop
        for i in range (random.randrange(5, 35)):
            for j in range(random.randrange(5, 25)):
                wall = arcade.Sprite("../Lab 09 - Sprites and Walls/box.png", SPRITE_SCALING_BOX)
                wall.center_x = 100 + j * 64
                wall.center_y = 100 + i * 64
                self.wall_list.append(wall)
                wall = arcade.Sprite("../Lab 09 - Sprites and Walls/box.png", SPRITE_SCALING_BOX)
                wall.center_x = 100 + i * 64
                wall.center_y = 100 + j * 64
                self.wall_list.append(wall)

        # --- Place hazards inside a loop
        for i in range(random.randrange(5, 35)):
            for j in range(random.randrange(5, 25)):
                hazard = arcade.Sprite("../Lab 09 - Sprites and Walls/hazard.png", SPRITE_SCALING_BOX)
                hazard.center_x = 100 + j * 64
                hazard.center_y = 100 + i * 64
                self.wall_list.append(hazard)
                hazard = arcade.Sprite("../Lab 09 - Sprites and Walls/hazard.png", SPRITE_SCALING_BOX)
                hazard.center_x = 100 + i * 64
                hazard.center_y = 100 + j * 64
                self.wall_list.append(hazard)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.hazard_list.draw()
        self.wall_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        self.physics_engine.update()

        changed = False

        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left - 1,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom - 1)

        if self.player_sprite.center_x < 0:
            self.player_sprite.center_x = 0
        if self.player_sprite.center_x > 3000:
            self.player_sprite.center_x = 3000
        if self.player_sprite.center_y < 0:
            self.player_sprite.center_y = 0
        if self.player_sprite.center_y > 3000:
            self.player_sprite.center_y = 3000

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
