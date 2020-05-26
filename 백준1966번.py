from collections import deque
def qu(N,M,li):
    queue=deque()
    count=0
    for i in range(len(li)):
        queue.append([li[i],i])
        
    while queue:
        p=0
        num,index1=queue.popleft()
        for j in range(len(queue)):
            if num<queue[j][0]:
                queue.append([num,index1])
                
                p=1
                break
        
        if p==0:
            count+=1
        if p==0 and index1==M:
            return print(count)

T=int(input())
for k in range(T):
    N,M=input().split()
    N=int(N)
    M=int(M)
    li=list(map(int,input().split()))
    qu(N,M,li)