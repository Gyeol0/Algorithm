import itertools
import copy
N,M=input().split()
N=int(N)
M=int(M)
graph=[]
li=[]
li2=[]
for i in range(N):
    a=list(map(int,input().split()))
    graph.append(a)
    for j in range(N):
        if a[j]==2:
            li.append([i,j])
        if a[j]==1:
            li2.append([i,j])
        
num=len(li)-M
com=list(itertools.combinations(li,num))
l=len(com)
sum2=[]
if l>1:
    for i in com:
        li3=copy.deepcopy(li)
        sum1=0
        
        for j in range(num):
            li3.remove(i[j])
        for k in li2:
            x1=k[0]
            y1=k[1]
            m=999999
            for p in li3:
                x2=p[0]
                y2=p[1]
                s=abs(x1-x2)+abs(y1-y2)
                if m>s:
                    m=s
            sum1+=m
        sum2.append(sum1)
    print(min(sum2))
else:
    sum1=0
    for i in li2:
        x1=i[0]
        y1=i[1]
        m=999999
        for p in li:
            x2=p[0]
            y2=p[1]
            s=abs(x1-x2)+abs(y1-y2)
            if m>s:
                m=s
        sum1+=m
    print(sum1)
