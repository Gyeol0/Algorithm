import math
T=int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    if (x1,y1,r1)==(x2,y2,r2):
        print(-1)
    else:
        l=math.sqrt((x1-x2)**2+(y1-y2)**2)
        if l==r1+r2:
            print(1)
        elif l>r1+r2:
            print(0)
        else:
            if l+min(r1,r2)==max(r1,r2):
                print(1)
            elif l+min(r1,r2)<max(r1,r2):
                print(0)
            else:
                print(2)