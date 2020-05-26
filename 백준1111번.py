N=int(input())
A=list(map(int,input().split()))
if N==1:
    print('A')
elif N==2:
    if A[0]==A[1]:
        print(A[0])
    else:
        print('A')
else:
    k1=A[2]-A[1]
    k2=A[1]-A[0]
    if k2==0 and k1!=0:
        print('B')
    elif k2!=0 and k1==0:
        a=k1//k2
        b=A[1]-A[0]*a
        answer=A[N-1]*a+b
        t=0
        for j in range(N-1):
            if A[j+1]!=A[j]*a+b:
                t=1
                break
        if t==0:
            print(answer)
        elif t==1:
            print('B')
    elif k2==0 and k1==0:
        a=1
        b=0
        t=0
        answer=A[N-1]*a+b
        for j in range(N-1):
            if A[j+1]!=A[j]*a+b:
                t=1
                break
        if t==0:
            print(answer)
        elif t==1:
            print('B')
    elif k2!=0 and k1!=0:
        
        a=k1//k2
        b=A[1]-A[0]*a
        answer=A[N-1]*a+b
        t=0
        for j in range(N-1):
            if A[j+1]!=A[j]*a+b:
                t=1
                break
        if t==0:
            print(answer)
        elif t==1:
            print('B')