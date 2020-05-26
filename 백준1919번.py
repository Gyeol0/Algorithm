A=input()
B=input()
A1={}
B1={}
for i in A:
    if i in A1:
        A1[i]+=1
    else:
        A1[i]=1
for i in B:
    if i in B1:
        B1[i]+=1
    else:
        B1[i]=1
sum1=0
for i in A1:
    if i in B1:
        sum1+=abs(A1[i]-B1[i])
    else:
        sum1+=A1[i]
for i in B1:
    if i not in A1:
        sum1+=B1[i]
print(sum1)