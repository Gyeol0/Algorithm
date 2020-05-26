from collections import deque
def aaa(M,N,K):
    queue=deque()
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    graph=[[0]*M for i in range(N)]
    count=2
    for i in range(K):
        b,a=input().split()
        a=int(a)
        b=int(b)
        graph[a][b]=1
    

    for j in range(N):
        for p in range(M):
            if graph[j][p]==1:
                queue.append([j,p])    
                while queue:
                    x,y=queue.popleft()
                    for i in range(4):
                        ax=x+dx[i]
                        ay=y+dy[i]
            
                        if ax>=0 and ax<N and ay>=0 and ay<M:
                            if graph[ax][ay]==1:
                                graph[ax][ay]=count
                                queue.append([ax,ay])
                count+=1
    print(count-2)
T=int(input())
for l in range(T):
    M,N,K=input().split()
    M=int(M)
    N=int(N)
    K=int(K)
    aaa(M,N,K)