N=int(input())
A=list(map(int,input().split()))
max1=-100000000000
min1=100000000000
for i in range(N):
    if max1<A[i]:
        max1=A[i]
    if min1>A[i]:
        min1=A[i]
print(min1,max1,end=' ')