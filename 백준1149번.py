N=int(input())
A=[[0]*3 for i in range(N)]
for i in range(N):
    A[i][0],A[i][1],A[i][2]=map(int, input().split())

B= [[0]*3 for i in range(N)]
        
for i in range(N):
    if i==0:
        B[i]=A[i]
    else:
        B[i][0]=A[i][0]+min(B[i-1][1],B[i-1][2])
        B[i][1]=A[i][1]+min(B[i-1][0],B[i-1][2])
        B[i][2]=A[i][2]+min(B[i-1][0],B[i-1][1])
print(min(B[N-1]))
