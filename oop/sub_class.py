class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


def make_animal_speak(animal: Animal):
    print(animal.speak())


def main():
    dog = Dog("buddy")
    cat = Cat("kitty")
    print(make_animal_speak(dog))
    print(make_animal_speak(cat))


if __name__ == "__main__":
    main()
