import itertools
from collections import deque
import copy
A,B,C=map(int,input().split())
max1=[A,B,C]
queue=deque()
answer=[]
li=list(map(list,itertools.permutations([0,1,2],3)))
queue.append([0,0,C])
visit=[]
visit.append([0,0,C])
while queue:
    K=queue.popleft()
    if K[0]==0:
        if K[2] not in answer:
            answer.append(K[2])
    for i in li:
        if K[i[0]]>0:
            
            for j in range(1,3):
                K1=copy.deepcopy(K)
                if K1[i[0]]>0:
                    k=max1[i[j]]-K1[i[j]]
                    if k>0:
                        if k>K1[i[0]]:
                            K1[i[j]]+=K1[i[0]]
                            K1[i[0]]=0
                            if K1 not in visit:
                                queue.append(K1)
                                visit.append(K1)
                        elif k<=K1[i[0]]:
                            K1[i[j]]+=k
                            K1[i[0]]-=k
                            if K1 not in visit:
                                queue.append(K1)
                                visit.append(K1)
answer.sort()
for i in answer:
    print(i,end=' ')