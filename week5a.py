# Base class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        print(f"I am {self.name} from {self.universe}, and my power is {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass with specific behavior (polymorphism)
class Speedster(Superhero):
    def __init__(self, name, universe):
        super().__init__(name, "Super Speed", universe)

    def use_power(self):
        print(f"{self.name} dashes at lightning speed! ⚡")

# Another subclass
class Telepath(Superhero):
    def __init__(self, name, universe):
        super().__init__(name, "Mind Control", universe)

    def use_power(self):
        print(f"{self.name} manipulates thoughts effortlessly. 🧠")

# Creating objects
flash = Speedster("Flash", "DC")
professor_x = Telepath("Professor X", "Marvel")

# Using methods
flash.introduce()
flash.use_power()

professor_x.introduce()
professor_x.use_power()
