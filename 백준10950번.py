T=int(input())
A=[]
B=[]
for i in range(T):
    a,b=input().split()
    A.append(int(a))
    B.append(int(b))
    
for i in range(T):
    print(A[i]+B[i])
