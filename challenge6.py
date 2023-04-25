#Written by Shiven Desai
class Automobiles: 
    def __init__(self, make, model, mileage, price):
        self._make = make
        self._model = model
        self._mileage = mileage
        self._price = price

    # these are the mutator methods
    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_mileage(self, mileage):
        self._mileage = mileage

    def set_price(self, price):
        self._price = price

    # these are the accessor methods
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


class Truck(Automobiles): 
    def __init__(self, make, model, mileage, price):
        Automobiles.__init__(self, make, model, mileage, price)


class SUV(Automobiles):
    def __init__(self, make, model, mileage, price):
        Automobiles.__init__(self, make, model, mileage, price)


class ElectricVehicle(Automobiles):
    def __init__(self, make, model, mileage, price, battery_life):
        Automobiles.__init__(self, make, model, mileage, price)
        self._battery_life = battery_life

    def set_battery_life(self, battery_life):
        self._battery_life = battery_life

    def get_battery_life(self):
        return self._battery_life


def main():
    used_car1 = Automobiles('Audi', 2022, 45000, 80000.0)
    used_car2 = Automobiles('Honda', 2022, 45000, 80000.0)

    print('Make: ', used_car1.get_make())
    print('Model: ', used_car1.get_model())
    print('Mileage: ', used_car1.get_mileage())
    print('Price: ', used_car1.get_price())
    print("\n")

    print('Make: ', used_car2.get_make())
    print('Model: ', used_car2.get_model())
    print('Mileage: ', used_car2.get_mileage())
    print('Price: ', used_car2.get_price())
    print("\n")

    truck = Truck('Toyota', 'Tacoma', 40000, 12000.0)
    suv = SUV('Volvo', 'SE', 30000, 18500.0)
    ev = ElectricVehicle('Tesla', 'Model S', 50000, 90000.0, 300)

    # display the truck's data
    print('The following truck is in inventory:')
    print('Make: ', truck.get_make())
    print('Model: ', truck.get_model())
    print('Mileage: ', truck.get_mileage())
    print('Price: ', truck.get_price())
    print("\n")

    # display the SUV's data 
    print('The following SUV is in inventory:')
    print('Make: ', suv.get_make()) 
    print('Model: ', suv.get_model()) 
    print('Mileage: ', suv.get_mileage()) 
    print('Price: ', suv.get_price()) 
    print("\n")

    # display the electric vehicle's data

# display the electric car's data
print('The following electric vehicle is in inventory:')
print('Make:', ev.get_make())
print('Model:', ev.get_model())
print('Mileage:', ev.get_mileage())
print('Price:', ev.get_price())
print('Battery Capacity:', ev.get_battery_capacity())

