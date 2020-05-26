M=int(input())
N=int(input())
sum1=0
min1=99999999999
for i in range(M,N+1):
    t=0
    if i==1 or i==0:
        continue
    elif i==2:
        sum1+=i
        if min1>i:
            min1=i
    else:
        
        for j in range(2,int(i//2)+2):
            if i%j==0:
                t=1
                break
        if t==0:
            sum1+=i
            if min1>i:
                min1=i
if sum1>0:
    
    print(sum1)
    print(min1)
else:
    print(-1)