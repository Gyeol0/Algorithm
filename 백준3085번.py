N=int(input())
graph=[]
dx=[0,1]
dy=[1,0]
max1=0
for _ in range(N):
    a=list(input())
    graph.append(a)
for i in range(N):
    for j in range(N):
        for k in range(2):
            x=i+dx[k]
            y=j+dy[k]
            if x>=0 and y>=0 and x<N and y<N:
                if graph[i][j]!=graph[x][y]:
                    graph[i][j],graph[x][y]=graph[x][y],graph[i][j]
                    
                    for p in range(N):
                        for q in range(N):
                            if q==0:
                                row_ch=graph[p][q]
                                count_row=1
                            else:
                                if graph[p][q]==row_ch:
                                    count_row+=1
                                else:
                                    if count_row>max1:
                                        max1=count_row
                                    row_ch=graph[p][q]
                                    count_row=1
                        
                            if q==0:

                                col_ch=graph[q][p]
                                count_col=1
                            else:
                                if graph[q][p]==col_ch:
                                    count_col+=1
                                else:
                                    if count_col>max1:
                                        max1=count_col
                                    col_ch=graph[q][p]
                                    count_col=1
                        if count_row>max1:
                            max1=count_row
                        if count_col>max1:
                            max1=count_col
                            
                    graph[i][j],graph[x][y]=graph[x][y],graph[i][j]
print(max1)