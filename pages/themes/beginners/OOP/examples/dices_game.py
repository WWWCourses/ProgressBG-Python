from random import randint
from time import sleep

class Die():
	"""docstring for Die"""
	def __init__(self):
		self.value = 555

	def throw(self):
		self.value = randint(1,6)

	def show(self):
		print(self.value)



die1 = Die()

print("I'm shuffling the die.")
die1.throw()
key = input("Press a key to stop...")

die1.show()
