words = input().split(',')
acr = input()
yes = 0
if len(words)==len(acr):
    for i in range(len(words)):
        if words[i][0]==acr[i]:
            yes = 1  
        else:
            yes = 0
if yes==0:
    print('Not an acronym')
else:
    print('Yes its an acronym')
    