A=[]
A.append(0)
A.append(1)
n=int(input())
for i in range(n-1):
    A.append(A[i]+A[i+1])
print(A[n])
