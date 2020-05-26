from collections import deque
N,M=input().split()
N=int(N)
M=int(M)
graph={}
visit=[]
A=[]
queue=deque()
count=0
for i in range(1,N+1):
    graph[i]=[]
    A.append(i)
for i in range(M):
    a,b=input().split()
    a=int(a)
    b=int(b)
    graph[a].append(b)
    graph[b].append(a)

while A:
    queue.append(A[0])
    vi=[]
    while queue:
        node=queue.popleft()
        if node not in vi:
            vi.append(node)
            if node in A:
                A.remove(node)
            queue.extend(graph[node])
    
    visit.append(vi)

print(len(visit))