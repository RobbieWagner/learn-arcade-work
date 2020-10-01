class Room:
    def __init__(self, description, north, south, east, west):
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.description = description


def main():
    done = False
    current_room = 0
    room_list = []

    # The list of rooms to be explored
    room = Room("You stand in the entryway of the small house.\nA coat rack stands in the corner with a gray pea coat and a hat.\nYou hear muffled television static through the door on the western wall.\nA flickering light floods into the entryway from the threshold on the northern wall", 2, None, None, 1)
    room_list.append(room)
    room = Room("You are now in what appears to be the living room.\nThe loud static of the TV fills the space.\nThere's books and clothes on the ground, smashed glass sprawled around, and furniture pushed carelessly on its side.\nThe door to the kitchen is blocked by an overturned bookshelf.\nWhat happened here?\nThe other door on the eastern wall leads back to the entryway, and there is a hallway south from the living room.", None, 3, 0, None)
    room_list.append(room)
    room = Room("The smell of mold and mildew fills your nostrils.\nYou stand in the dirty kitchen.\nA single lightbulb hangs from the center of the room, flickering on and off.\n You attempt to open the door on the western wall, but something is blocking it from the other side.\nThe door on the southern wall leads back to the entryway", None, 0, None, None)
    room_list.append(room)
    room = Room("An overturned lamp rests on the ground in the hallway.\nThe lampshade is bent and the cord is torn and frayed.\n A drawing, something that looks like it was made by a little kid, sits on the wall.\nTwo stick figures hold hands, and the smaller one has a blue teddy bear.\nThere is a stair case east from the hall.\nTelevision static blares from the living room north of the hallway.", 1, None, 4, None)
    room_list.append(room)
    room = Room("You the large creaking of loose steps as your foot falls on each one.\nPictures of similar looking people stare at you with fake smiles.\nThe second floor rests at the top of the stairs north of the landing.\nThe first floor lies down the stairs, west of the landing.", 5, None, None, 3)
    room_list.append(room)
    room = Room("There's a wilted fern at the top of the steps.\nIts brown color is deeper than the wooden floor under it.\nThe hallway continues all the way to a wall on the northern side of the house.\nThere's an awful smell coming from behind the door on your left.\nThe stairs behind you go down to the first floor.", 7, 4, None, 6)
    room_list.append(room)
    room = Room("The only thing illuminating the bathroom is natural light from an open window by the sink.\n The sink itself has a leak.\nIts drips echo off the walls.\nIts hard to tell where the smell is coming from, but you don't really want to know.\nThere's a door on the northern wall with scuff marks on the bottom.\nThe door to the hallway rests on the eastern wall.", 8, None, 5, None)
    room_list.append(room)
    room = Room("A draft breezes through the open window, sending in a cool overcast air.\nWind blows at the curtains, flaring them upwards slightly.\nThere is more hallway in the southern direction.\nA door sits ajar on the western wall", None, 5, None, 8)
    room_list.append(room)
    room = Room("A bed sits on the northwestern corner of the room.\nIt's skewed as if it were pushed, and the bedsheets droop off of it, touching the floor.\nThere's a small trail of small red stains dotting a path to the door on the southern wall.\nThe door on the eastern wall stands ajar.", None, 6, 7, None)
    room_list.append(room)

    while done == False:
        print()
        print(room_list[current_room].description)
        action = str(input("You decide to walk "))

        # Has you move north if possible
        if action.lower() == "n" or action.lower() == "north":
            if room_list[current_room].north == None:
                print("\nYou cannot move in that direction")
            else:
                current_room = room_list[current_room].north

        # Has you move west ifpossible
        elif action.lower() == "w" or action.lower() == "west":
            if room_list[current_room].west == None:
                print("\nYou cannot move in that direction")
            else:
                current_room = room_list[current_room].west

        # Has you move south if possible
        elif action.lower() == "s" or action.lower() == "south":
            if room_list[current_room].south == None:
                print("\nYou cannot move in that direction")
            else:
                current_room = room_list[current_room].south

        # Has you move east if possible
        elif action.lower() == "e" or action.lower() == "east":
            if room_list[current_room].east == None:
                print("\nYou cannot move in that direction")
            else:
                current_room = room_list[current_room].east

        # Quits the exploration
        elif action.lower() == "q" or action.lower() == "quit":
            print("You've spent enough time here anyway.")
            done = True

        else:
            print("\nYour input is misunderstood. Please try again.")


main()
