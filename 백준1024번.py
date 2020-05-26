N,L=input().split()
N=int(N)
L=int(L)
A=[]
for i in range(L,101):
    k=(N-((i-1)*i)/2)
    if k%i==0 and k>=0:
        for j in range(i):
            A.append((k/i)+j)
        break
if len(A)==0:
    print(-1)
else:
    for i in range(len(A)):
        print(int(A[i]),end=' ') 