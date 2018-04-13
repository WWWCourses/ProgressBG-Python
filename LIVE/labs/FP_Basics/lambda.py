def add(f1,f2):
  return f1(2,3) + f2(3)

print(add( lambda n,a: n**a , lambda n: 2*n ))





