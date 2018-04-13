from random import randint

class Die():
	"""docstring for Die"""
	def __init__(self):
		self.value = None

	def throw(self):
		self.value = randint(1,6)

	def show(self):
		print(self.value)


die1 = Die()
die2 = Die()

for i in range(1000):
	die1.throw()
	die2.throw()
	if die1.value == 6 and die2.value == 6:
		print("Dueshesh on try {}".format(i+1))
		break
