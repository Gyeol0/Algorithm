import itertools
N=int(input())
num=N//2
li=[i for i in range(N)]
st=list(map(list,itertools.combinations(li,num)))
l=len(st)
link=sorted(st,reverse=True)
S=[]

for i in range(N):
    a=list(map(int,input().split()))
    S.append(a)
min1=999999999999    
for i in range(l):
    
    sum1=0
    sum2=0
    for k in range(num-1):
        s1=st[i][k]
        l1=link[i][k]
        for p in range(k+1,num):
            s2=st[i][p]
            l2=link[i][p]
            sum1+=S[s1][s2]
            sum1+=S[s2][s1]
            sum2+=S[l1][l2]
            sum2+=S[l2][l1]
        
    if abs(sum1-sum2)<min1:
        min1=abs(sum1-sum2)
            

print(min1)        