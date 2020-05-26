N,M=map(int,input().split())
check=[False]*(N+1)
num=[0]*M
def aa(a,n,m):
    if a==m:
        for i in range(m):
            print(num[i],end=' ')
        print()
        return
    for i in range(1,n+1):
        if check[i]:
            continue
        check[i]=True
        num[a]=i
        aa(a+1,n,m)
        check[i]=False
aa(0,N,M)