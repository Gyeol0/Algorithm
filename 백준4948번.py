while True:
    n=int(input())
    if n==0:
        break
    A=[False,False]+[True]*(2*n-1)
    B=[]
    for i in range(2,2*n+1):
        if A[i]:
            B.append(i)
            for j in range(2*i,2*n+1,i):
                A[j]=False
    count=0
    for i in B:
        if i>n:
            count+=1
    print(count)