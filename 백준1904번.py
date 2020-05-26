N=int(input())
A=[0 for i in range(N)]
for i in range(N):
    if i==0:
        A[i]=1%15746
    elif i==1:
        A[i]=2%15746
    else:
        A[i]=(A[i-1]+A[i-2])%15746
print(A[N-1])
        
