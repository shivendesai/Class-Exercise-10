#Written by Shiven Desai
class Automobiles: 
    def __init__(self, make, model, mileage, price):
        self._make = make 
        self._model = model 
        self._mileage = mileage 
        self._price = price 

    #these are the mutator methods 
    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_mileage(self, mileage):
        self._mileage = mileage

    def set_price(self, price):
        self._price = price

    #these are the accessor methods
    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_mileage(self): 
        return self._mileage

    def get_price(self): 
        return self._price

def main(): 
    used_car = Automobiles('Audi', 2022, 45000, 80000.0)
    print('Make: ', used_car.get_make()) 
    print('Model: ', used_car.get_model()) 
    print('Mileage: ', used_car.get_mileage())
    print('Price: ', used_car.get_price()) 

    new_car = Automobiles('Toyota', 2023, 20000, 35000.0)
    print('\nMake: ', new_car.get_make()) 
    print('Model: ', new_car.get_model()) 
    print('Mileage: ', new_car.get_mileage())
    print('Price: ', new_car.get_price()) 

main() 
