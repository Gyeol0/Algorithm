T=int(input())
for _ in range(T):
    n=int(input())
    if n==0:
        break
    m=int(n**0.5)
    A=[False,False]+[True]*(n-1)
    B=[]
    for i in range(2,m+1):
        if A[i]:
            for j in range(2*i,n+1,i):
                A[j]=False
    for i in range(n+1):
        if A[i]==True:
            B.append(i)
    l=len(B)
    max1=max([i for i in range(l) if B[i]<=n//2])
    t=0
    for i in range(max1,-1,-1):
        if t==1:
            break
        for j in range(i,l):
            if B[i]+B[j]==n:
                print(B[i],B[j])
                t=1
                break