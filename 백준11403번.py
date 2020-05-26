N=int(input())
graph={}
queue=[]
for i in range(N):
    a=list(map(int, input().split()))
    k=[]
    for j in range(N):
        if a[j]==1:
            k.append(j)
    graph[i]=k


answer=[[0]*N for i in range(N)]

for i in range(N):
    visit=[]
    queue.append(i)
    while queue:
        node=queue.pop(0)
        
        if node not in visit:
            if i!=node:
                answer[i][node]=1
            visit.append(node)
            queue.extend(graph[node])
            
        else:
            if i==node:
                answer[i][i]=1

for i in range(N):
    for j in range(N):
        print(answer[i][j], end=' ')
    print()