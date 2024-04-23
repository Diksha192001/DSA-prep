def numberCrown(n: int) -> None:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        # print()
        print(" "*(n-i), end="")

        for y in range(i, 0, -1):
            print(y, end=" ")
        print()

#take input
n = int(input())
numberCrown(n)
