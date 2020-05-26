T=int(input())    
def steak():
    a=[]
    b=[]
    n=int(input())
    li1=input().split(' ')
    li2=input().split(' ')
    for i in range(n):
        li1[i]=int(li1[i])
        li2[i]=int(li2[i])
    a.append(li1[0])
    b.append(max(li1[0],li2[0]))
    a.append((li2[0]+li1[1]))
    b.append((li1[0]+li2[1]))
    for i in range(2,n):
        a.append(max(b[i-1],b[i-2])+li1[i])
        b.append(max(a[i-1],a[i-2])+li2[i])
    maxA=max(a)
    maxB=max(b)
    maximum=max(maxA,maxB)
    print(maximum)

for j in range(T):
    steak()
        
