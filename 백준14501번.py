N=int(input())
T=[0 for i in range(N)]
P=[0 for i in range(N)]
Max=0
def aaa(i,c):
    global Max
    if i+T[i]==N:
        if c+P[i]>Max:
            Max=c+P[i]
    elif i+T[i]>N:
        if c>Max:
            Max=c
    else:
        for j in range(i+T[i],N):
            aaa(j,c+P[i])        
     
for i in range(N):
    T[i],P[i] =input().split()
    T[i]=int(T[i])
    P[i]=int(P[i])

for i in range(N):
    aaa(i,0)
    
print(Max)