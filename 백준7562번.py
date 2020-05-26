from collections import deque
def night(l,start,end):
    graph=[[0]*l for _ in range(l)]
    queue=deque()
    dx=[1,-1,1,-1,2,2,-2,-2]
    dy=[2,2,-2,-2,1,-1,1,-1]
    queue.append([start[0],start[1],0])
    graph[start[0]][start[1]]=1
    
    while queue:
        x,y,count=queue.popleft()
        if x==end[0] and y==end[1]:
            break
        for i in range(8):
            ax=x+dx[i]
            ay=y+dy[i]
            
            if ax>=0 and ax<l and ay>=0 and ay<l:
                if graph[ax][ay]==0:
                    graph[ax][ay]=1
                    queue.append([ax,ay,count+1])

    return print(count)
    
T=int(input())
for _ in range(T):
    l=int(input())
    start=list(map(int,input().split()))
    end=list(map(int,input().split()))
    night(l,start,end)