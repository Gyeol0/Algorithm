import heapq

N,K=map(int,input().split())
G=[]
C=[]
for _ in range(N):
    a,b=map(int,input().split())
    heapq.heappush(G,[a,b])
for _ in range(K):
    C.append(int(input()))
C.sort()
answer=[]
answer_1=[]
for i in C:
    while len(G)>0 and i>=G[0][0]:
        heapq.heappush(answer,-heapq.heappop(G)[1])
    if len(answer)!=0:
        answer_1.append(-heapq.heappop(answer))
    elif len(G)==0:
        break
print(sum(answer_1))