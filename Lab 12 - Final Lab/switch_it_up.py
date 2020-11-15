import random


def reset_the_board(grid, rows, columns, full_array1, full_array2):
    # strips the board
    grid *= 0

    # recreates an empty board
    for row in range(rows):
        grid.append([])
        for column in range(columns):
            grid[row].append([])

    # gives each box a unique color
    for row in range(rows):
        for column in range(columns):
            checking = True
            some_value = 0

            # picks a color, and assigns it if it is unique
            while checking:
                color_value = random.randrange(9)
                for checking_row in range(rows):
                    for checking_column in range(columns):
                        if grid[checking_row][checking_column] != color_value:
                            some_value += 1
                        if some_value == columns * rows:
                            checking = False
                        elif checking_row == rows - 1 and checking_column == columns - 1:
                            some_value = 0

            grid[row][column] = color_value

    full_array1 *= 0
    full_array2 *= 0
