# A person needs to offer lemons to God. He needs 21 of them. But the lemons present with him vary. So we need to print appropriate message to him to ensure that correct number of lemons are considered.

n=int(input("Enter the number of lemons you have: "))
num=21
print('Sufficient lemons') if (n==num) else print('buy', num-n, 'more lemons') if (n<num) else print(n-num, 'extra lemons present') if (n>num) else print('dont enter negative values') if (n<0) else print("Enter correct amount")
