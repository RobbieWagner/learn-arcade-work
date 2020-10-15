""" Sprites and Walls Lab
Sprites created in piskelapp.com by me. (There's a reason I didn't go to art school)."""

import arcade
import random

# --- Constants ---
pennies = 15
walls = 8

SPRITE_SCALING_BOX = 2
SPRITE_SCALING_PLAYER = 4

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

MOVEMENT_SPEED = 5

VIEWPORT_MARGIN = SCREEN_HEIGHT/2

# sound from Kenny.nl
good_sound = arcade.load_sound("impactMining_003.ogg")


class MyGame(arcade.Window):
    """This class creates the main game window"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "This is the Best Game that has Ever Been Made")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.penny_list = None

        self.score = 0

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        self.view_left = 0
        self.view_bottom = 0

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.PALE_PLUM)

        self.view_left = 0
        self.view_bottom = 0

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.penny_list = arcade.SpriteList()

        self.score = pennies

        # Create the player (graphic made in Piskel)
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        self.player_list.append(self.player_sprite)

        # --- Place boxes inside a loop (graphics made in Piskel)

        for j in range(walls):
            for i in range(random.randrange(25, 30)):
                wall = arcade.Sprite("hazard.png", SPRITE_SCALING_BOX)
                wall.center_x = 512 * (j + 1)
                wall.center_y = (i + 1) * 64
                self.wall_list.append(wall)

        for j in range(walls):
            for i in range(random.randrange(25, 30)):
                wall = arcade.Sprite("hazard.png", SPRITE_SCALING_BOX)
                wall.center_x = 512 * (j + 1)
                wall.center_y = 4096 - (i + 1) * 64
                self.wall_list.append(wall)

        for i in range(126):
            wall = arcade.Sprite("box.png", SPRITE_SCALING_BOX)
            wall.center_x = i * 64
            wall.center_y = 64
            self.wall_list.append(wall)

        for i in range(126):
            wall = arcade.Sprite("box.png", SPRITE_SCALING_BOX)
            wall.center_x = 64
            wall.center_y = i * 64
            self.wall_list.append(wall)

        for i in range(126):
            wall = arcade.Sprite("box.png", SPRITE_SCALING_BOX)
            wall.center_x = i * 64
            wall.center_y = 4096
            self.wall_list.append(wall)

        for i in range(126):
            wall = arcade.Sprite("box.png", SPRITE_SCALING_BOX)
            wall.center_x = 4096
            wall.center_y = i * 64
            self.wall_list.append(wall)

        for k in range(10):
            wall = arcade.Sprite("hazard_2.png", SPRITE_SCALING_BOX)
            wall.center_x = random.randrange(128, 4096, 64)
            wall.center_y = random.randrange(1984, 2240, 64)
            self.wall_list.append(wall)

        for m in range(int((pennies + 1) / 2)):
            penny = arcade.Sprite("penny.png", SPRITE_SCALING_BOX)
            penny.center_x = 512 * (m + 1) - 224
            penny.center_y = 2560
            self.penny_list.append(penny)

        for m in range(int((pennies - 1) / 2)):
            penny = arcade.Sprite("penny.png", SPRITE_SCALING_BOX)
            penny.center_x = 512 * (m + 2) - 224
            penny.center_y = 1664
            self.penny_list.append(penny)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()
        self.penny_list.draw()

        output = f"Pennies Left: {self.score}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20, arcade.color.GREEN, 20)

        if len(self.penny_list) == 0:
            arcade.draw_text("You Got All of the Pennies!",
                             self.view_left + SCREEN_WIDTH/2 - 200,
                             self.view_bottom + SCREEN_HEIGHT/2,
                             arcade.color.GREEN,
                             25)

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
        if self.player_sprite.center_x > 5000:
            self.player_sprite.center_x = 5000
        if self.player_sprite.center_y < 0:
            self.player_sprite.center_y = 0
        if self.player_sprite.center_y > 5000:
            self.player_sprite.center_y = 5000

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.penny_list)

        for penny in hit_list:
            penny.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(good_sound, 5)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if len(self.penny_list) > 0:
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
