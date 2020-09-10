import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SEEDS = 4
PARASITES = 4
POS_IN_LINE = SCREEN_WIDTH / 5


def draw_rind():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT/8, 0, arcade.color.GREEN)
    arcade.draw_lrtb_rectangle_filled(SCREEN_WIDTH/5, SCREEN_WIDTH*2/5, SCREEN_HEIGHT/8, 0, arcade.color.DARK_GREEN)
    arcade.draw_lrtb_rectangle_filled(SCREEN_WIDTH*3/5, SCREEN_WIDTH*4/5, SCREEN_HEIGHT/8, 0, arcade.color.DARK_GREEN)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT/8+5, SCREEN_HEIGHT/8, arcade.color.WHITE)


def draw_seed(x, y):
    arcade.draw_parabola_filled(x, y, x + 20, 15,
                                arcade.color.BLACK_OLIVE, 180)
    arcade.draw_triangle_filled(x, y + 15, x + 20, y + 15,
                                x + 10, y + 35, arcade.color.BLACK_OLIVE)


def draw_pearl_string(x, y):
    arcade.draw_circle_filled(x, y, 15, arcade.color.PEARL)
    arcade.draw_circle_filled(x-25, y+15, 15, arcade.color.PEARL)
    arcade.draw_circle_filled(x+25, y+15, 15, arcade.color.PEARL)
    arcade.draw_circle_filled(x+50, y+30, 15, arcade.color.PEARL)
    arcade.draw_circle_filled(x-50, y+30, 15, arcade.color.PEARL)


def add_seeds():
    seed_pos = POS_IN_LINE
    for i in range(SEEDS):
        draw_seed(seed_pos, 100)
        seed_pos += SCREEN_WIDTH/5


def draw_parasite(x, y):
    arcade.draw_parabola_outline(x,
                                 y, x + 20, 20, arcade.color.FOREST_GREEN, 6, 0)
    arcade.draw_parabola_outline(x + 20,
                                 y, x + 50, 20, arcade.color.FOREST_GREEN, 6, 180)
    arcade.draw_parabola_outline(x + 90,
                                 y, x + 120, 20, arcade.color.FOREST_GREEN, 6, 0)
    arcade.draw_parabola_outline(x + 120,
                                 y, x + 140, 20, arcade.color.FOREST_GREEN, 6, 180)
    arcade.draw_circle_filled(x + 70,
                              y, 30, arcade.color.FOREST_GREEN)
    arcade.draw_parabola_outline(x,
                                 y - 20, x + 20, 20, arcade.color.FOREST_GREEN, 6, 0)
    arcade.draw_parabola_outline(x + 20,
                                 y - 20, x + 40, 20, arcade.color.FOREST_GREEN, 6,
                                 180)
    arcade.draw_parabola_outline(x + 100,
                                 y - 20, x + 120, 20, arcade.color.FOREST_GREEN, 6,
                                 0)
    arcade.draw_parabola_outline(x + 120,
                                 y - 20, x + 140, 20, arcade.color.FOREST_GREEN, 6,
                                 180)
    arcade.draw_circle_filled(x + 70,
                              y, 10, arcade.color.BLACK)


def add_parasites():
    parasite_pos = POS_IN_LINE
    for i in range(PARASITES):
        draw_parasite(parasite_pos, 300)
        parasite_pos += SCREEN_WIDTH / 5


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Robbie's Watermelon Land")
    arcade.set_background_color(arcade.color.PERSIAN_RED)
    arcade.start_render()

    draw_rind()
    add_seeds()
    add_parasites()
    draw_pearl_string(400, 500)

    arcade.finish_render()
    arcade.run()


main()
