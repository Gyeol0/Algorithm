import math as mt
N=int(input())
A=[0 for i in range(N+1)]
A[0]=9999999
if N==1:
    print(1)
elif N==2:
    print(2)

else:
    A[1]=1
    A[2]=2
    for i in range(1,N+1):
        if int(mt.sqrt(i))==mt.sqrt(i):
            A[i]=1
        else:
            a=999999
            k1=int(mt.sqrt(i))
            for j in range(1,k1+1):
                if a>1+A[i-j**2]:
                    a=1+A[i-j**2]
        
            A[i]=a
            
    print(A[N])