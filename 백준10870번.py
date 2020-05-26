def pibo(n,arr):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    
    else:
        k1=arr[-1]
        k2=arr[-2]
        arr.append(k1+k2)
        if len(arr)==n+1:
            return arr[n]
        else:
            return pibo(n,arr)
N=int(input())
arr=[0,1,1]
print(pibo(N,arr))