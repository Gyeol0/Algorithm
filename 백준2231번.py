N=int(input())
a=0
k=N
A=[]

while(1):
    k=k/10
    a+=1
    if int(k)==0:
        break
    
for i in range(N):
    B=[]
    for j in range(a):
        B.append(int((i%(10**(j+1)))/(10**j)))
    if i+sum(B)==N:
        A.append(i)    
if len(A)==0:
    print(0)
else:
    print(min(A))

