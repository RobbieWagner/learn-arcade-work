"""
This program is a rendition of Camel, called Shia.
In this game, you run for your life from Shia LaBeouf
as depicted in the viral YouTube video "Shia LaBeouf Live"
By Rob Cantor
https://www.youtube.com/watch?v=o0u4M6vppCI
Above is the link to the original video, which is the
inspiration behind this game.
"""

import random


def main():

    miles_traveled = 0
    shias_miles_traveled = -18
    bandage_age = 0
    batteries = 3
    done = "n"
    battery_mortality = 0
    goal = 200
    friend = 0

    print("""
----------------------------------------------------------
Welcome to Shia! (Trigger warning for violence, gore, and murder)
----------------------------------------------------------
    
The legends about the park are true. 
    
While camping with some friends, you hear footsteps approach.
One of your friends screams as they fall, and a pool of blood soaks into the ground.
You immediately look at the axe in their head.
    
He's here.
    
Out of panic, you and your friends run in different directions and scatter.
Another axe swings at you, slicing down a large portion of your abdomen.
After running away for what feels like forever, your body takes over, forcing you to rest.
    
Shia is no longer after you, but is still nearby.
    
You bandage up your bleeding torso, and pull the flashlight and extra batteries from your backpack.
A map nearby shows you the quickest way out: a windy trail almost TWENTY MILES in length.
Before you begin the trek, you hear one of your other friend's screams in the distance.
    
Shia is nearby.
And he isn't finished hunting.
    
----------------------------------------------------------   
""")

    while done != "q":
        print("""A. Replenish Flashlight Batteries
B. Follow Path
C. Risk a Shortcut
D. Stop to Change Bandages
E. Analyze Your Situation
Q. Quit Game
""")
        action = str(input("Your instincts tell you to... "))
        if action.lower() == "q":
            print("""
Thank you for playing, and remember...
Shia is always watching.
""")
            done = "q"
        elif action.lower() == "a":
            if batteries > 0:
                batteries -= 1
                battery_mortality = 0
                print("\nYou replaced your flashlight batteries, the forest seems a little more bright\n")
            else:
                print("\nYou ran out of batteries\n")
        elif action.lower() == "b":
            friend = random.randrange(1, 51)
            gain = random.randrange(5, 13)
            shias_gain = random.randrange(7, 15)
            battery_mortality += 1
            bandage_age += 1
            miles_traveled += gain
            shias_miles_traveled += shias_gain
            print("\nYou traveled ", gain / 10, " miles\n")
        elif action.lower() == "c":
            friend = random.randrange(1, 51)
            gain = random.randrange(10, 21)
            shias_gain = random.randrange(7, 15)
            battery_mortality += 1
            bandage_age += random.randrange(1, 4)
            miles_traveled += gain
            shias_miles_traveled += shias_gain
            print("\nYou traveled ", gain/10, " miles\n")
        elif action.lower() == "d":
            shias_gain = random.randrange(7, 15)
            shias_miles_traveled += shias_gain
            bandage_age = 0
            print("You replaced your bloody bandages with new ones")
        elif action.lower() == "e":
            print("Distance Covered: ", miles_traveled/10, " miles")
            print("Batteries Left: ", batteries)
            distance = miles_traveled-shias_miles_traveled
            print("He is ", distance/10, " miles away")
        else:
            print("""That is not an appropriate response, please select the letter that corresponds to your choice
Example: you want to risk a shortcut, you think Shia is close and you want to increase your distance,
you type in c, or C
""")
        if battery_mortality > 6:
            print("""Your flashlight flickers on and off more, violently trying to stay alive.
You take a few more steps, hoping it won't go out.
""")
            if miles_traveled < goal:
                print("You only have ", (goal-miles_traveled)/10, " miles left to travel.\n")
            print("You take only a few more steps before it goes out for good.")
            if batteries > 0:
                print("You scrounge in your backpack, trying to find the last batteries in the dark.")
            else:
                print("You walk along the road more in the dark. It's hard to see even a few feet ahead.")
            print("""You hear rustling in the surrounding bushes. Your legs quake before taking over.
You are now running down the dark road. You stumble on a rock and fall to your face,
dropping your flashlight. Shia emerges from the shrubs with a knife.
He walks towards you, the sound of each step quickening your heartbeat

You are dead.""")
            done = "q"
        elif battery_mortality > 3 and bandage_age < 10:
            print("Your flashlight is flickering. You may need more batteries.")
        if bandage_age > 9:
            print("""Despite the heavy bleeding of your abdomen, you continue to move on.
Blood soaks your clothes and hands. Some gets on the head of your flashlight,
bathing everything you look at in dim red light. You press on a little more.""")
            if miles_traveled < goal:
                print("\nYou only have ", (goal-miles_traveled)/10, " miles left to travel.\n")
            print("""An axe flies out of nowhere. The blunt end of it sweeps your feet,
sending you to the ground. He's standing over you now, holding a machete.
You are helpless to fight as the machete sinks into your chest.

You are dead.
""")
            done = "q"
        elif bandage_age > 5:
            print("The blood begins to soak through your bandages.")
        if miles_traveled - shias_miles_traveled <= 0:
            print("""You watch Shia appear from behind a tree holding a shovel
He gets down on all fours and begins sprinting towards you.
You try to run away, but he's too fast

You are dead.""")
            if miles_traveled < goal:
                print("\nYou only have ", (goal-miles_traveled)/10, " miles left to travel.\n")
            print("""Shia knocks you to the ground, towering over you.
Consciousness fades as he hits you over the head with the shovel""")
            done = "q"
        elif miles_traveled - shias_miles_traveled <= 15:
            print("\nHe's getting closer.\n")
        if miles_traveled >= goal:
            print("""You walk out of the park, and into a nearby town.
After calling the police, they escort you to the local hospital.
You escaped Shia LaBeouf""")
            done = "q"
        if friend == 50:
            friend = 0
            print("""You notice a small trail of blood along the path.
It's one of your friends, and they are covered in blood.
You walk closer. You don't have time to stop and mourn,
and you won't make it out with what you have.

Batteries replenished
You replaced your bloody bandages with new ones
""")
            bandage_age = 0
            batteries += 3
        if friend == 13:
            print("You hear te scream of one of your friends in the distance.")
        if friend == 8:
            print("You notice a pool of blood on the ground. It looks new.")
        if friend == 7 or friend == 4:
            print("A small group of ravens fly past your face, cawing loudly.")
        if friend == 1:
            print("You hear a tree fall.")
        if friend == 25:
            print("It's raining.")


main()

