str1 = input().replace(' ', '').lower()

m=0
for i in str1:
    if str1.count(i)>1:
        str1 = str1.replace(i, '')
        str1 = str1+i
for i in str1:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        m+=1
if m==26:
    print('panagram')
else:
    print('not a panagram')
        
