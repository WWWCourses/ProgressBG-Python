class NumbersIterator:	
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.num = start - 1

	def __next__(self):		
		self.num += 1	
		if self.num<=self.end:			
			return self.num
		else:
			raise StopIteration

	def __iter__(self):
		return self
	


ni = NumbersIterator(1,5)

for i in ni:
	print( i )

