import math
M=int(input())
N=int(input())
k=int(math.sqrt(M))
li=[]
while k**2<=N:
    if k**2>=M:
        li.append(k**2)
    k+=1
if len(li)==0:
    print(-1)
else:
    print(sum(li))
    print(min(li))