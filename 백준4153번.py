while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    max1=max(a,b,c)
    if 2*max1**2==a**2+b**2+c**2:
        print('right')
    else:
        print('wrong')