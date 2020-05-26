from collections import deque
N,K=input().split()
N=int(N)
K=int(K)
graph=[0 for i in range(100001)]
queue=deque()
queue.append([N,1])
graph[K]=-1
graph[N]=1

while queue:
    x,count=queue.popleft()
    if x==K:
        break
    d=[1,-1,x]
    
    for i in range(3):
        ax=x+d[i]
        if ax>=0 and ax<100001:
            if graph[ax]==0 or graph[ax]==-1:
                graph[ax]=count+1
                queue.append([ax,count+1])
            elif count+1<graph[ax]:
                graph[ax]=count+1
                queue.append([ax,count+1])
print(count-1)