class Dog():
    def __init__(self):
        self.name = ""
        self.age = 0

    def bark(self):
        print("Woof", self.name)


def main():
    my_dog = Dog()
    my_dog.name = "Rover"
    my_dog.age = 2
    my_dog.bark()


main()
