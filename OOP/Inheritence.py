# inheritence means a child object inherits
# aspects of its parent class (methods, attributes)

class Vehicle:
    def __init__(self, speed, year):
        self.speed = speed
        self.year = year

    def start(self):
        print("You started the vehicle")
    
    def data(self):
        print(f"The vehicle is from {self.year}.")

class Plane(Vehicle):
    def fly(self):
        print("The plane has taken off!")

boeing = Plane(100, 2012)

boeing.start()
boeing.fly()
boeing.data()