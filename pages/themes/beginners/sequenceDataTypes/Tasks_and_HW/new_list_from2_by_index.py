first_names = ["ivan", "maria", "petar"]
sur_names = ["ivanov", "popova", "petrov"]
names = []


# names = [
#    
# ]

for i in range(0,3,1):
   names = names + [ first_names[i], sur_names[i] ]

print(names)
