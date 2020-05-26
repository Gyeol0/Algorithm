N,M=input().split()
N=int(N)
M=int(M)
A=input().split()
B=[]
for i in range(len(A)):
    A[i]=int(A[i])
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i!=j and j!=k and i!=k:
                if A[i]+A[j]+A[k]<=M:
                    B.append(A[i]+A[j]+A[k])
print(max(B))
   
