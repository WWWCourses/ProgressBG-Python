def simple_generator():
  yield 1
  yield 2
  
  
sg = simple_generator()
print( next(sg) )
print( next(sg) )

# print(sg.__next__())
# print(sg.__next__())
# print(sg.__next__())
# print(sg.__next__())