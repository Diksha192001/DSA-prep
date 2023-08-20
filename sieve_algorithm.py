#sieve algorithm
nos = []
num = int(input('Enter the number till which you want to calculate prime nos: '))
for a in range(2, num):
    nos.append(a)

limit = num
x=2
while x<limit+1:
    if x**2<=limit:
        x = x+1
    else:
        break
x = x-1

for i in range(2, x+1):
    for j in range(i+1, num):
        if (j%i==0):
            if j in nos:
                nos.remove(j)
print(nos)
