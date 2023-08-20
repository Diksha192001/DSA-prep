#print neon numbers
neons = []
for num in range(1, 1000): 
    sq = num**2
    dig_sum = 0
    while sq>0:
        dig_sum = dig_sum + sq%10
        sq = sq//10
        print(sq)
    if num//10==0:
        if dig_sum == num:
            neons.append(num)
            print(neons)
    else:
        print("not neon")
print(neons)
