class Person:
	def __init__(self, fname, Iname):
		self.firstname = fname
		self.lastname = Iname

	def printname(self):
		print(self.firstname, self.lastname)

class Student(Person):
	def __init__(self, fname, Iname, year):
		super().__init__(fname, Iname)
		self.graduationyear = year
		
x = Student("Joey", "King", 2021)
x.printname()
print(x.graduationyear) 