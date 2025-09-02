# Question 3: Inheritance Practice
# You are building a system for an animal shelter.
# Design a base class Animal with shared attributes and methods.
# Then create two subclasses: Dog and Cat, each with their own behavior.

# Question 4: Polymorphism in Action
# You now have a base class Animal and subclasses Dog and Cat.
# Your task is to:
# Add a method make_sound() in the Animal class (e.g., "makes a sound").
# Override this method in Dog (say "Woof!") and Cat (say "Meow!").
# Then show how a for loop over a list of animals can call the correct make_sound() dynamically (i.e., polymorphism in action).
class Animal:
    def __init__(self, species: str, age: int, name: str, color: str ):
        self._species=species
        self._age=age
        self._name=name
        self._color=color
    @property
    def species(self) -> str:
        return self._species
    @property
    def age(self) -> int:
        return self._age
    @property
    def name(self) -> str:
        return self._name
    @property
    def color(self) -> str:
        return self._color

    def make_sound(self):
        return "Animal makes sound"


    def __str__(self):
        return f"Species: {self._species}||Age: {self._age}||Name: {self.name}||Color: {self.color}"

class Dog(Animal):
    def __init__(self, age: int, name: str, color: str):
        super().__init__("Canis lupus familiaris", age, name, color)
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, age: int, name: str, color: str):
        super().__init__("Felis catus", age, name, color)
    def make_sound(self):
        return "Meow!"



def main():
    animals = [Dog(3, "Buddy", "Brown"), Cat(2, "Whiskers","White")]
    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")
main()