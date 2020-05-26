T=int(input())
A=[]
B=[]
B.append(1)
B.append(1)
B.append(1)
for i in range(T):
    A.append(int(input()))
for i in range(3,max(A)):
    B.append(B[i-2]+B[i-3])
for i in range(T):
    print(B[A[i]-1])
