from collections import deque
K=int(input())
W,H=input().split()
W=int(W)
H=int(H)
graph=[]
queue=deque()
dx=[0,0,1,-1,1,-1,1,-1,-2,-2,2,2]
dy=[1,-1,0,0,2,2,-2,-2,1,-1,1,-1]


for i in range(H):
    a=list(map(int,input().split()))
    graph.append(a)
    
queue.append((0,0,K,0))
kk=[[-1]*W for i in range(H)]
graph[0][0]=2
while queue:
    x,y,k,count=queue.popleft()
    if x==H-1 and y==W-1:
        break
    if k>0:
        p=12
    else:
        p=4
    for i in range(p):
        ax=x+dx[i]
        ay=y+dy[i]
        if ax>=0 and ax<H and ay>=0 and ay<W:
            if i>3:
                a=k-1
            else:
                a=k
            if graph[ax][ay]==0:
                graph[ax][ay]=2
                queue.append((ax,ay,a,count+1))
                kk[ax][ay]=a
                
            elif graph[ax][ay]==2:
                if kk[ax][ay]!=-1 and kk[ax][ay]<a:
                    kk[ax][ay]=a
                    queue.append((ax,ay,a,count+1))
                

if graph[H-1][W-1]==0:
    print(-1)
else:
    print(count)