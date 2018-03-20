sum = 0

first_num = 1000
last_num = 1200

num = first_num
while num <= last_num:
    if num%2 == 0:
        sum += num
    num += 1

print(sum)
