first_names = ["ivan", "maria", "petar"]
sur_names = ["ivanov", "popova", "petrov"]

# names will store the third list. In the beginning it's empty:
names = []

# make the third list:
for i in range(len(first_names)):
    names = names + [first_names[i], sur_names[i]]

print(names)
