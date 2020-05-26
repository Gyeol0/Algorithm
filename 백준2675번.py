T=int(input())
for _ in range(T):
    N,S=input().split()
    N=int(N)
    S=list(S)
    P=''
    for i in S:
        for j in range(N):
            P+=i
    print(P)