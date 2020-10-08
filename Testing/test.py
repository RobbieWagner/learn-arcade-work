"""import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3


class Fairy:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class Boy:
    def __init__(self, position_x, position_y, radius, color, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x
        if self.position_x < self.radius:
            self.position_x = self.radius
        if self.position_y < self.radius:
            self.position_y = self.radius


class Hazard:
    def __init__(self, position_x1, position_x2, position_y1, position_y2, color):
        self.position_x1 = position_x1
        self.position_x2 = position_x2
        self.position_y1 = position_y1
        self.position_y2 = position_y2
        self.color = color

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.position_x1, self.position_x2, self.position_y1, self.position_y2,
                                          self.color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title, lives):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.fairy = Fairy(50, 50, 3, arcade.color.PINK)
        self.boy = Boy(45, 45, 12, arcade.color.WHITE, 0, 0)
        self.hazard = Hazard(100, 200, 200, 100, arcade.color.EERIE_BLACK)
        self.lives = lives

    def on_draw(self):
        arcade.start_render()
        self.fairy.draw()
        self.boy.draw()
        self.hazard.draw()
        output = "Lives: " + str(self.lives)
        arcade.draw_text(output, 10, 20, arcade.color.BLUE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.fairy.position_x = x
        self.fairy.position_y = y

    def update(self, delta_time):
        self.boy.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.boy.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.boy.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.boy.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.boy.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.boy.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.boy.change_y = 0
# define the boy and fairy as sprites


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Fairy", 3)

    arcade.run()


main()"""

# Write your function below:
def is_list_sorted(list):
  x = 0
  for i in range(len(list)-1):
    if list[i] < list[i+1]:
      x += 1
  if x + 1 == len(list):
    return True
  return False

# This is some code you can use to test:

# Example 1, should print False
my_list = [0, 3, -1, 8]
result = is_list_sorted(my_list)
print("Example 1:", result)

# Example 2, should print True
my_list = [-100, -80, 0, 20, 40, 99, 101]
result = is_list_sorted(my_list)
print("Example 2:", result)