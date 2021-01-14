from collections import deque
M,N=map(int,input().split())
graph=[]
check=0
for i in range(N):
    a=list(input())
    for j in range(len(a)):
        if a[j]=='C' and check==0:
            start=[i,j]
            a[j]='S'
            check+=1
    graph.append(a)
queue=deque()
dx=[0,1,0,-1,0]
dy=[0,0,-1,0,1]
di=[1,2,3,4]
queue.append(start+[1,0])
queue.append(start+[2,0])
queue.append(start+[3,0])
queue.append(start+[4,0])
min_count=99999999999
while queue:
    x,y,dire,count=queue.popleft()
    for i in range(1,5):
        ax=x+dx[i]
        ay=y+dy[i]
        if ax>=0 and ay>=0 and ax<N and ay<M:
            if dire==1:
                if i==2 or i==4:
                    if graph[ax][ay]=='.':
                        graph[ax][ay]=count+1
                        queue.append([ax,ay,i,count+1])
                    elif graph[ax][ay]!='*' and graph[ax][ay]!='C':
                        if graph[ax][ay]>=count+1:
                           graph[ax][ay]=count+1
                           queue.append([ax,ay,i,count+1])
                    elif graph[ax][ay]=='C':
                        if min_count>count+1:
                            min_count=count+1
                            
                elif i==1:
                    if graph[ax][ay]=='.':
                        graph[ax][ay]=count
                        queue.append([ax,ay,i,count])
                    elif graph[ax][ay]!='*' and graph[ax][ay]!='C':
                        if graph[ax][ay]>=count:
                            graph[ax][ay]=count
                            queue.append([ax,ay,i,count])
                    elif graph[ax][ay]=='C':
                        if min_count>count:
                            min_count=count
            elif dire==2:
                if i==1 or i==3:
                    if graph[ax][ay]=='.':
                        graph[ax][ay]=count+1
                        queue.append([ax,ay,i,count+1])
                    elif graph[ax][ay]!='*' and graph[ax][ay]!='C':
                        if graph[ax][ay]>=count+1:
                           graph[ax][ay]=count+1
                           queue.append([ax,ay,i,count+1])
                    elif graph[ax][ay]=='C':
                        if min_count>count+1:
                            min_count=count+1
                            
                elif i==2:
                    if graph[ax][ay]=='.':
                        graph[ax][ay]=count
                        queue.append([ax,ay,i,count])
                    elif graph[ax][ay]!='*' and graph[ax][ay]!='C':
                        if graph[ax][ay]>=count:
                            graph[ax][ay]=count
                            queue.append([ax,ay,i,count])
                    elif graph[ax][ay]=='C':
                        if min_count>count:
                            min_count=count
            elif dire==3:
                if i==2 or i==4:
                    if graph[ax][ay]=='.':
                        graph[ax][ay]=count+1
                        queue.append([ax,ay,i,count+1])
                    elif graph[ax][ay]!='*' and graph[ax][ay]!='C':
                        if graph[ax][ay]>=count+1:
                           graph[ax][ay]=count+1
                           queue.append([ax,ay,i,count+1])
                    elif graph[ax][ay]=='C':
                        if min_count>count+1:
                            min_count=count+1
                            
                elif i==3:
                    if graph[ax][ay]=='.':
                        graph[ax][ay]=count
                        queue.append([ax,ay,i,count])
                    elif graph[ax][ay]!='*' and graph[ax][ay]!='C':
                        if graph[ax][ay]>=count:
                            graph[ax][ay]=count
                            queue.append([ax,ay,i,count])
                    elif graph[ax][ay]=='C':
                        if min_count>count:
                            min_count=count                            
            elif dire==4:
                if i==1 or i==3:
                    if graph[ax][ay]=='.':
                        graph[ax][ay]=count+1
                        queue.append([ax,ay,i,count+1])
                    elif graph[ax][ay]!='*' and graph[ax][ay]!='C':
                        if graph[ax][ay]>=count+1:
                           graph[ax][ay]=count+1
                           queue.append([ax,ay,i,count+1])
                    elif graph[ax][ay]=='C':
                        if min_count>count+1:
                            min_count=count+1
                            
                elif i==4:
                    if graph[ax][ay]=='.':
                        graph[ax][ay]=count
                        queue.append([ax,ay,i,count])
                    elif graph[ax][ay]!='*' and graph[ax][ay]!='C':
                        if graph[ax][ay]>=count:
                            graph[ax][ay]=count
                            queue.append([ax,ay,i,count])
                    elif graph[ax][ay]=='C':
                        if min_count>count:
                            min_count=count                    
            
print(min_count)