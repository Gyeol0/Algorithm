L=input()
al=['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
    'O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=[0 for i in range(26)]
L=L.upper()
for i in L:
    index1=al.index(i)
    num[index1]+=1
max1=max(num)
if num.count(max1)>1:
    print('?')
else:
    index2=num.index(max1)
    print(al[index2])