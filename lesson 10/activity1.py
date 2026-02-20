# parent class
class Person(object):

	# constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

# child class

class Employee(Person):

	def __init__(self, name, idnumber, salary, post):
		# calling parent constructor
		Person.__init__(self, name, idnumber)

		# child class attributes
		self.salary = salary
		self.post = post

# creating object

a = Employee('Penguin', 20210401, 15000, "Intern")

# calling parent class function

a.display()