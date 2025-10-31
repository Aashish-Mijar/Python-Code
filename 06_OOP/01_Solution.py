# ----- Creation of class and Objects
class Car:
    # brand = None
    # model = None
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

 # instantiated object       
my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.brand)