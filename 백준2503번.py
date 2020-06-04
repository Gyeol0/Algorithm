import copy
N=int(input())
li=[i for i in range(100,1000)]
for i in range(N):
    n,s,b=map(int,input().split())
    li1=[]
    for j in li:
        s1=0
        b1=0
        p1=j//100
        p2=(j//10)%10
        p3=j%10
        q1=n//100
        q2=(n//10)%10
        q3=n%10
        if p1==p2 or p1==p3 or p2==p3 or p2==0 or p3==0:
            continue
        
        if p1==q1:
            s1+=1
        if p2==q2:
            s1+=1
        if p3==q3:
            s1+=1
        if p1==q2 or p1==q3:
            b1+=1
        if p2==q1 or p2==q3:
            b1+=1
        if p3==q1 or p3==q2:
            b1+=1
            
        if b1==b and s1==s:
            li1.append(j)
    li=copy.deepcopy(li1)
print(len(li))