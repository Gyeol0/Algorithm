N=int(input())
count=0
for i in range(1,N+1):
    if i<10:
        count+=1
    elif i<100:
        count+=1
    elif i<1000:
        a1=int(i/100)
        a2=int((i-a1*100)/10)
        a3=i-a1*100-a2*10
        if a2*2==a1+a3:
            count+=1
print(count)