N=int(input())
A=[]
B=[]
C=[]
D=[]
for _ in range(N):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
AB={}
CD={}      
for i in A:
    for j in B:
        if i+j not in AB: #get 사용해도 가능
            AB[i+j]=1
        else:
            AB[i+j]+=1
for i in C:
    for j in D:
        if i+j not in CD:
            CD[i+j]=1
        else:
            CD[i+j]+=1

answer=0
for i in AB.keys(): #두 집합으로 묶어 절댓값이 같도록 하는 순서쌍
    if -i in CD.keys():
        answer+=AB[i]*CD[-i]
        
print(answer)