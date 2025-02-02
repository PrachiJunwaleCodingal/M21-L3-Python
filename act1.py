#Is this a bus
class vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

class bus(vehicle):
    pass

bus1= vehicle("Tata", 100, 10)
print("bus name:",bus1.name)
print("bus speed:",bus1.speed)
print("bus mileage:",bus1.mileage)