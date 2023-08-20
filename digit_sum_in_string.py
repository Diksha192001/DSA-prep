str = 'jammu99kashmir75'
sum = 0
newsum = 0
for i in range(len(str)):
    if str[i].isnumeric():
        sum = sum+int(str[i])
    else:
        i = i+1
print('sum after for loop:', sum)
newsum = sum
while newsum//10!=0:
    newsum = 0
    while sum>0:
        newsum = newsum + (sum%10)
        sum = sum//10
print(newsum)
