class Car:
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    
    def __str__(self):
        return f"{self.name} is a {self.color} {self.kind} worth ${self.value:.2f}"

class Racecar(Car):
    def __init__(self, name, color, value):
        Car.__init__(self, name, "racecar", color, value)

class Towtruck(Car):
    def __init__(self, name, color, value):
        Car.__init__(self, name, "towtruck", color, value)