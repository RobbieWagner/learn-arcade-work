""" in this lab, I will be making a watermelon themed picture,
 because watermelon is great and I couldn't think of anything else
"""

# get the commands for this lab with arcade
import arcade

# make watermelon colored background
arcade.open_window(800, 600, "Robbie's Watermelon")
arcade.set_background_color(arcade.color.PERSIAN_RED)

# once that is set up, I need to set up for drawing
arcade.start_render()

# time to draw the watermelon

# first, the rind
arcade.draw_lrtb_rectangle_filled(0, 800, 75, 0, arcade.color.GREEN)
arcade.draw_lrtb_rectangle_filled(160, 320, 75, 0, arcade.color.DARK_GREEN)
arcade.draw_lrtb_rectangle_filled(480, 640, 75, 0, arcade.color.DARK_GREEN)
arcade.draw_lrtb_rectangle_filled(0, 800, 80, 75, arcade.color.WHITE)

"""
all these rectangles are making this drawing a square
let's add something fun!
"""

# Seed 1
arcade.draw_parabola_filled(70, 400, 90, 15, arcade.color.BLACK_OLIVE, 180)
arcade.draw_triangle_filled(70, 415, 90, 415, 80, 435, arcade.color.BLACK_OLIVE)

# Seed 2
arcade.draw_parabola_filled(170, 250, 190, 15, arcade.color.BLACK_OLIVE, 180)
arcade.draw_triangle_filled(170, 265, 190, 265, 180, 285, arcade.color.BLACK_OLIVE)

# Seed 3
arcade.draw_parabola_filled(400, 300, 420, 15, arcade.color.BLACK_OLIVE, 180)
arcade.draw_triangle_filled(400, 315, 420, 315, 410, 335, arcade.color.BLACK_OLIVE)

# Seed 4
arcade.draw_parabola_filled(470, 105, 490, 15, arcade.color.BLACK_OLIVE, 180)
arcade.draw_triangle_filled(470, 120, 490, 120, 480, 140, arcade.color.BLACK_OLIVE)

# Finally, seed 5
arcade.draw_parabola_filled(700, 475, 720, 15, arcade.color.BLACK_OLIVE, 180)
arcade.draw_triangle_filled(700, 490, 720, 490, 710, 510, arcade.color.BLACK_OLIVE)

# Alien parasite
arcade.draw_parabola_outline(600, 200, 620, 20, arcade.color.FOREST_GREEN, 6, 0)
arcade.draw_parabola_outline(620, 200, 650, 20, arcade.color.FOREST_GREEN, 6, 180)
arcade.draw_parabola_outline(690, 200, 720, 20, arcade.color.FOREST_GREEN, 6, 0)
arcade.draw_parabola_outline(720, 200, 740, 20, arcade.color.FOREST_GREEN, 6, 180)
arcade.draw_circle_filled(670, 200, 30, arcade.color.FOREST_GREEN)
arcade.draw_parabola_outline(600, 180, 620, 20, arcade.color.FOREST_GREEN, 6, 0)
arcade.draw_parabola_outline(620, 180, 640, 20, arcade.color.FOREST_GREEN, 6, 180)
arcade.draw_parabola_outline(700, 180, 720, 20, arcade.color.FOREST_GREEN, 6, 0)
arcade.draw_parabola_outline(720, 180, 740, 20, arcade.color.FOREST_GREEN, 6, 180)
arcade.draw_circle_filled(670, 200, 10, arcade.color.BLACK)

# Use functions to keep window up and run the function
arcade.finish_render()
arcade.run()
