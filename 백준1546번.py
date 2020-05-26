N=int(input())
A=list(map(int,input().split()))
max1=max(A)
for i in range(N):
    A[i]=A[i]/max1*100
print(sum(A)/N)