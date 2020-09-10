game_over = True

if game_over:
    print("a is true")

game_over = False

a = True
b = True

if a and b:
    print("YES")
else:
    print("NO")

temperature = input("What is the temperature in Fahrenheit? ")
temperature = float(temperature)

if 90 < temperature <= 150:
    print("It is hot outside")
elif temperature > 150:
    print("Get inside! the planet is on fire!!!!!!")
else:
    temperature = str(temperature)
    print("it is " + temperature + " degrees outside. Not too bad!")
