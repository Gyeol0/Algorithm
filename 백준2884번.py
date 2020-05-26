H,M=map(int,input().split())
if M>=45:
    M-=45
elif M<45:
    if H>0:
        H-=1
        M+=15
    elif H==0:
        H=23
        M+=15
print(H,M,end=' ')