T=int(input())
A=[]
B=[]
for i in range(T):
    a,b=input().split()
    A.append(int(a))
    B.append(int(b))
    
for i in range(1,T+1):
    print('Case #{}: {}'.format(i,A[i-1]+B[i-1]))

