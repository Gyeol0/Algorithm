N=int(input())
A=[[0]*2 for i in range(N)]
B=[1 for i in range(N)]
for i in range(N):
    A[i]=list(map(int,input().split()))
for i in range(N):
    count=0
    for j in range(N):
        if i!=j:
            if A[i][0]<A[j][0] and A[i][1]<A[j][1]:
                B[i]+=1
for i in range(N):
    print(B[i],end=' ')