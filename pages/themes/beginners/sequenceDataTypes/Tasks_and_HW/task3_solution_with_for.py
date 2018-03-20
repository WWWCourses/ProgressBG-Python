# in the beginning the sum is 0:
sum = 0

# add each number to the current sum:
for i in range(1000, 1201):
	# you can skip next line, if you add step 2 as range
  if i % 2 == 0:
      sum += i
print(sum)
