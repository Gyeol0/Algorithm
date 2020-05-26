N,X=input().split()
N=int(N)
X=int(X)
A=input().split()
B=[]
for i in range(len(A)):
    A[i]=int(A[i])
    if X>A[i]:
        print(A[i],end=' ')
