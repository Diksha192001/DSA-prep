# Catalan number
def catalan(n):
    cat = [0]*n
    cat[0] = 1
    cat[1] = 1
    if n>0:
        for i in range(2, n):
            for j in range(0, i):
                cat[i] += cat[j]*cat[i-j-1]
                print("cat[i]=", cat[i] )
    return cat
n = int(input('enter the total catalan numbers you want to be printed: '))
print(catalan(n))
