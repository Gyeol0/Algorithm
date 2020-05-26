def bfs(graph,start):
    visit=[]
    queue=[]
    
    queue.append(start)
    
    while queue:
        node=queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    
    return visit

def dfs(graph,start):
    visit=[]
    stack=[]
    
    stack.append(start)
    
    while stack:
        node=stack.pop()
        if node not in visit:
            visit.append(node)
            graph[node].reverse()
            stack.extend(graph[node])
    
    return visit

N,M,V=input().split()
N=int(N)
M=int(M)
V=int(V)
graph={}

for i in range(1,N+1):
    graph[i]=[]
for i in range(M):
    a,b=input().split()
    graph[int(a)].append(int(b))
    graph[int(b)].append(int(a))
for i in range(1,N+1):
    graph[i].sort()
    
bf=bfs(graph,V)
df=dfs(graph,V)



for j in range(len(df)):
    print(df[j],end=' ')
print()
for i in range(len(bf)):
    print(bf[i],end=' ')    
