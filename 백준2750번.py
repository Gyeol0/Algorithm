N=int(input())
A=[]
for i in range(N):
    k=int(input())
    A.append(k)
A.sort()
for i in range(N):
    print(A[i])