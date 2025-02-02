
#ACP- Bus fare
class vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 50

class bus(vehicle):
    def fare(self):
        amt = super().fare()
        amt =amt+ amt * 0.1
        return amt

obj = bus("volvo", 40)
print("Bus fare:", obj.fare())