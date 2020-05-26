T=int(input())
for _ in range(T):
    k=int(input())
    n=int(input())
    A=[i for i in range(1,n+1)]
    for i in range(k):
        for j in range(n):
            if j==0:
                A[j]=1
            else:
                A[j]=A[j]+A[j-1]
    print(A[n-1])