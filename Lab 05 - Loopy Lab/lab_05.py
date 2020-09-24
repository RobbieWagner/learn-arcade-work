import arcade


def draw_section_outlines():
    # Draws the squares
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 5
            y = row * 10 + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        for column in range(30):
            if column % 2 == 1:
                color = arcade.color.BLACK
            else:
                color = arcade.color.WHITE
            x = column * 10 + 305
            y = row * 10 + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_3():
    for row in range(30):
        if row % 2 == 1:
            color = arcade.color.BLACK
        else:
            color = arcade.color.WHITE
        for column in range(30):
            x = column * 10 + 605
            y = row * 10 + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_4():
    for row in range(30):
        for column in range(30):
            if column % 2 == 0 and row % 2 == 0:
                color = arcade.color.WHITE
            else:
                color = arcade.color.BLACK
            x = column * 10 + 905
            y = row * 10 + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_5():
    for row in range(30):
        for column in range(row):
            x = 300 - column * 10 - 5
            y = 600 - row * 10 - 5
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    for row in range(30):
        for column in range(row + 2):
            y = 300 + column * 10 - 5
            x = 600 - row * 10 - 5
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():
    for row in range(30):
        for column in range(row + 1):
            y = 600 - column * 10 - 5
            x = 900 - row * 10 - 5
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    for row in range(30):
        for column in range(row + 1):
            y = 600 - column * 10 - 5
            x = 900 + row * 10 + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
