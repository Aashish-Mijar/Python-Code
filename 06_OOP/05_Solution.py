class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
    

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Bugati", "Model S", "85KWH")
# print(my_tesla.__brand)
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())


