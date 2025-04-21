class Vehicle:
    def move(self):
        print("The vehicle moves...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road! 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky! ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the sea! 🚢")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
