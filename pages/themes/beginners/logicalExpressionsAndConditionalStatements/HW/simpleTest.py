from random import randint
machine_number = randint(1, 10)

print("machine_number= {}".format(machine_number))


# one user move
user_number = (int(input("Your guess:")))

if user_number == machine_number:
    print("Congratulations!That's the number!")
elif user_number > machine_number:
    print("Lower!")
elif user_number < machine_number:
    print("Higher!")
else:
    pass
