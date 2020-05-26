X=int(input())
k=0
sum1=0
while sum1<X:
    k+=1
    sum1+=k
    
a=sum1-X+1
if X==1:
    answer='1/1'
else:
    count=k+1
    m=count-a
    if k%2==0:
        
        answer=str(m)+'/'+str(a)
    elif k%2!=0:
        answer=str(a)+'/'+str(m)
print(answer)