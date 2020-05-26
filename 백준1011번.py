import math
T=int(input())
for _ in range(T):
    x,y=map(int,input().split())
    d=y-x
    if d<=3:
        answer=d
    else:
        k=int(math.sqrt(d))
        if d==k**2:
            answer=2*k-1
        elif d<=k**2+k and d>k**2:
            answer=2*k
        else:
            answer=2*k+1
    print(answer)