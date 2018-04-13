class Person:
	def __init__(self, name, age):
		self.name = name
		self.__age = age

maria = Person("Maria Popova", 25)

# inspect object attributes dictionary:
print( maria.__dict__ )

# inspect class attributes dictionary:
print( Person.__dict__ )

print("maria has next attributes:")
print( maria.__dir__() )