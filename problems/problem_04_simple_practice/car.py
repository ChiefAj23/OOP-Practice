# What is the difference between a class and an object in Python?
# Can you create a simple class Car and create an object from it?

class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand=brand
        self.model=model
        self.year=year
    def __str__(self):
        return f"{self.brand}||{self.model}||{self.year}"


def main():
    c1=Car("Honda","CRV",2024)
    return print(c1)
main()