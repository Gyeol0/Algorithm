N=int(input())
A=[N]
p=-1
count=0
while p!=A[0]:
    a=A[-1]//10
    b=A[-1]%10
    M=a+b
    m=M%10
    p=b*10+m
    A.append(p)
    count+=1
print(count)
