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
import random


def selection_sort(my_list):
    """ Sort a list using the selection sort """

    run_time_inside = 0
    run_time_outside = 0

    # Loop through the entire array
    for cur_pos in range(len(my_list)):
        # Find the position that has the smallest number
        # Start with the current position

        run_time_outside += 1

        min_pos = cur_pos

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):

            run_time_inside += 1

            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # It is, mark this position as the smallest
                min_pos = scan_pos

        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

    print("Times Outside Loop Ran: ",run_time_outside)
    print("Times Inside Loop Ran: ",run_time_inside)


def insertion_sort(my_list):
    """ Sort a list using the insertion sort """

    run_time_inside = 0
    run_time_outside = 0

    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(my_list)):

        run_time_outside += 1

        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):

            run_time_inside += 1

            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value

    print("Times Outside Loop Ran: ", run_time_outside)
    print("Times Inside Loop Ran: ", run_time_inside)


# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():
    # Create two lists of the same random numbers
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 100
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    # Print the original list
    print("Original List")
    print_list(list_for_selection_sort)

    # Use the selection sort and print the result
    print("Selection Sort")
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)

    # Use the insertion sort and print the result
    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)


main()
