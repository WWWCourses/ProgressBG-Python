print("{:~^50}".format(" Simple while loop "))
i = 1
while i<=5 :
	print(i)
	i += 1


print("{:~^50}".format(" Example of else clause in while "))
i = 1
while i <= 5:
	# if i==3 : break
	print(i)
	i += 1
else :
	print("Condition is not true when i = ", i)
