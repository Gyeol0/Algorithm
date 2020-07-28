from collections import deque
n=int(input())
a,b=map(int,input().split())
m=int(input())
graph={}
for i in range(m):
    x,y=map(int,input().split())
    if x not in graph:
        graph[x]=[y]
    else:
        graph[x].append(y)
    if y not in graph:
        graph[y]=[x]
    else:
        graph[y].append(x)
queue=deque()
visit=[]
queue.append(a)
answer=0
end=0
while queue:
    l=len(queue)
    for i in range(l):
        k=queue.popleft()
        if k==b:
            end=1
            break
        if k not in visit:
            visit.append(k)
            queue.extend(graph[k])
    if end==1:
        break
    if len(queue)==0:
        answer=-1
        break
    answer+=1
print(answer)