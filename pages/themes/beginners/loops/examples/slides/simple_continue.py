print("IF: print all numbers in [1..5], nut skip 3")
i = 0
while i<5:
    i += 1
    if i==3:
        pass
    else:
        print(i)    


print("\nCONTINUE: print all numbers in [1..5], nut skip 3")
i = 0
while i < 5:
    i += 1
    if i == 3:
       continue
    print(i)    
