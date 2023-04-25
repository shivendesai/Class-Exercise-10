#Written by Shiven Desai
class Automobiles: 
    def __init__(self, make, model, mileage, price, doors):
        self._make = make 
        self._model = model 
        self._mileage = mileage 
        self._price = price 
        self._doors = doors

    # Mutator methods
    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_mileage(self, mileage):
        self._mileage = mileage

    def set_price(self, price):
        self._price = price

    def set_doors(self, doors):
        self._doors = doors

    # Accessor methods
    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_mileage(self): 
        return self._mileage

    def get_price(self): 
        return self._price

    def get_doors(self):
        return self._doors


def main(): 
    used_car = Automobiles('Audi', 2022, 45000, 80000.0, 4)
    print('Make: ', used_car.get_make()) 
    print('Model: ', used_car.get_model()) 
    print('Mileage: ', used_car.get_mileage())
    print('Price: ', used_car.get_price()) 
    print('Doors: ', used_car.get_doors())

    new_car = Automobiles('Ford', 2021, 20000, 40000.0, 2)
    print('\nMake: ', new_car.get_make()) 
    print('Model: ', new_car.get_model()) 
    print('Mileage: ', new_car.get_mileage())
    print('Price: ', new_car.get_price()) 
    print('Doors: ', new_car.get_doors())

    # Test mutator method
    used_car.set_doors(2)
    print('\nUsed car doors: ', used_car.get_doors())


if __name__ == '__main__':
    main()
