#issubclass() gives true  if inheritance is there
class Vehicles:
	def __init__(self):
		print("Its a parent class")


class bus(Vehicles):
	def __init__(self):
		Vehicles.__init__('bus')


print(issubclass(bus, Vehicles))
print(issubclass(bus, bus))
print(issubclass(bus, list))
