import sys
N=int(input())
arr=[0]*10001
for i in range(N):
    k=int(sys.stdin.readline())
    arr[k]+=1
for i in range(10001):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)
