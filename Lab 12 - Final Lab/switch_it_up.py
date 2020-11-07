import random


def reset_the_board(grid, rows, columns,):
    # gives each box a unique color
    for row in range(rows):
        for column in range(columns):
            checking = True
            some_value = 0

            # picks a color, and assigns it if it is unique
            while checking:
                color_value = random.randrange(9)
                print("color", color_value)
                for checking_row in range(rows):
                    for checking_column in range(columns):
                        if grid[checking_row][checking_column] != color_value:
                            some_value += 1
                            print(some_value)
                        if some_value == columns * rows:
                            print("color", color_value)
                            checking = False
                        elif checking_row == rows - 1 and checking_column == columns - 1:
                            some_value = 0

            grid[row][column] = color_value
