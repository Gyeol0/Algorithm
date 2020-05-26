M,N=map(int,input().split())
A=[False,False]+[True]*(N-1)
B=[]
for i in range(2,N+1):
    if A[i]:
        B.append(i)
        for j in range(2*i,N+1,i):
            A[j]=False
for i in B:
    if i>=M:
        print(i)