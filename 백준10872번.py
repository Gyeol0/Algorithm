def fac(n,k):
    if n==0:
        return 1
    elif n-1==0:
        return k
    else:
        k*=n
        return fac(n-1,k)
N=int(input())
print(fac(N,1))