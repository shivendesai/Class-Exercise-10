#Written by Shiven Desai
class Insect:
    def __init__(self, name, wings):
        self.name = name
        self.wings = wings

    def set_name(self, name):
        self.name = name

    def set_wings(self, wings):
        self.wings = wings

    def get_name(self):
        return self.name

    def get_wings(self):
        return self.wings


class Bumblebee(Insect):
    def __init__(self, name, wings, pollen_collector):
        super().__init__(name, wings)
        self.pollen_collector = pollen_collector

    def set_pollen_collector(self, pollen_collector):
        self.pollen_collector = pollen_collector

    def get_pollen_collector(self):
        return self.pollen_collector

    def fly(self):
        print("The bumblebee flies from flower to flower to collect nectar.")

    def buzz(self):
        print("The bumblebee makes a loud buzzing sound as it flies.")


class Grasshopper(Insect):
    def __init__(self, name, wings, jump_height):
        super().__init__(name, wings)
        self.jump_height = jump_height

    def set_jump_height(self, jump_height):
        self.jump_height = jump_height

    def get_jump_height(self):
        return self.jump_height

    def jump(self):
        print("The grasshopper can jump up to", self.jump_height, "times its body length.")

    def chirp(self):
        print("The grasshopper chirps by rubbing its legs together.")


# Testing the classes
bumblebee = Bumblebee("Buzzy", 4, True)
print("Name:", bumblebee.get_name())
print("Number of Wings:", bumblebee.get_wings())
print("Pollen Collector:", bumblebee.get_pollen_collector())
bumblebee.fly()
bumblebee.buzz()
print()

grasshopper = Grasshopper("Hopper", 2, 20)
print("Name:", grasshopper.get_name())
print("Number of Wings:", grasshopper.get_wings())
print("Jump Height:", grasshopper.get_jump_height())
grasshopper.jump()
grasshopper.chirp()
