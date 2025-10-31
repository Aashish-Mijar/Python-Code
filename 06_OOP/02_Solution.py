# Using of constructor in python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"Car: {self.brand} Model:{self.model}"

my_Car = Car("Toyota", "Corolla")

print(my_Car.full_name())