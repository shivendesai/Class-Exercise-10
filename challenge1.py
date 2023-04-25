#Written by Shiven Desai
class AnimalType:
    def eats(self):
        print("This animal likes to eat 2")

class rabbits(AnimalType):
    def munch(self):
        print(" carrots ")

class birds(rabbits):
    def munchl(self):
        print(" seeds ")

class cats(AnimalType):
    def eats(self):
        print("This animal likes to eat fish")

RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()

BirdObject = birds()
BirdObject.eats()
BirdObject.munchl()

CatObject = cats()
CatObject.eats()
