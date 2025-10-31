# --- Encapsulation----
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand
    

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    @staticmethod   #--- Decorators
    def general_description():
        return "Cars are means of transpotation"
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Bugati", "Model S", "85KWH")
my_Car = Car("Tata", "Nexon")
my_Car.model = "City"
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.full_name())

# print(my_Car.general_description())
# print(Car.general_description())

print(my_Car.model)

print(my_Car.model)