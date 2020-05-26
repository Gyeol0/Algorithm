A=[0 for i in range(9)]
B=[]
for i in range(9):
    A[i]=int(input())
Sum=sum(A)-100
del1=0
del2=0
for i in range(9):
    for j in range(9):
        if i==j:
            continue
        else:
            if A[i]+A[j]==Sum:
                del1=A[i]
                del2=A[j]
A.remove(del1)
A.remove(del2)
for i in range(len(A)):
    for j in range(i,len(A)):
        if A[i]>A[j]:
            A[i],A[j]=A[j],A[i]
for i in range(len(A)):
    print(A[i])