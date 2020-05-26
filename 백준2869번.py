A,B,V=map(int,input().split())
V1=V-A
if V1==0:
    count=1
else:
    count=V1//(A-B)
    if count*(A-B)==V1:
        count=count+1
    else:
        count=count+2
print(count)