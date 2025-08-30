# Question 3: Inheritance Practice
# You are building a system for an animal shelter.
# Design a base class Animal with shared attributes and methods.
# Then create two subclasses: Dog and Cat, each with their own behavior.

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

    def __str__(self):
        return f"Species: {self._species}||Age: {self._age}||Name: {self.name}||Color: {self.color}"

class Dog(Animal):
    def __init__(self, age: int, name: str, color: str):
        super().__init__("Canis lupus familiaris", age, name, color)

class Cat(Animal):
    def __init__(self, age: int, name: str, color: str):
        super().__init__("Felis catus", age, name, color)



def main():
    d1=Dog(3, "Buddy", "Brown")
    c1=Cat(2, "Whiskers","White")
    print(d1)
    print(c1)
main()