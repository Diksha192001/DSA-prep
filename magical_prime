n = int(input())

def prime(n):
    temp = 0
    for i in range(2, n):
        if n%i == 0:
            temp = 1
    if temp==1:
        return 0
    else:
        return 1

def reverse(n):
    revno = 0
    while n!=0:
        digit = n%10
        revno = revno*10 + digit
        n=n//10
    return revno

x = prime(n)
new = reverse(n)
print(new)
newx = prime(new)
if x==newx and x:
    print("magical prime")
else:
    print("not a magical prime")
