T=int(input())
A=[]
B=[]
for i in range(T):
    a,b=input().split()
    A.append(int(a))
    B.append(int(b))
for i in range(T):
    print('Case #{}: {} + {} = {}'.format(i+1,A[i],B[i],A[i]+B[i]))
