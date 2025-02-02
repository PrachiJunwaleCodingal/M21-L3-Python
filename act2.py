#employee inheritance
class person(object):		
		def __init__(self, name, id):
				self.name = name
				self.id = id
		def display(self):
				print(self.name)
				print(self.id)


class emp(person):		
		def __init__(self, name, id, salary, post):
				self.salary = salary
				self.post = post
				person.__init__(self, name, id)

		
obj = emp('Prachi', 1234, 50000, "Office Employee")	
obj.display()
