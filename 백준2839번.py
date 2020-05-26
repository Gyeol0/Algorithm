N=int(input())
k=N//5
answer=0
for i in range(k,-1,-1):
    if (N-i*5)%3==0:
        k1=(N-i*5)//3
        answer=i+k1
        break
if answer==0:
    print(-1)
else:
    print(answer)