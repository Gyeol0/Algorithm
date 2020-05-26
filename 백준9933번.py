N=int(input())
password=[]
length=[]
for _ in range(N):
    S=input()
    password.append(S)
    length.append(len(S))
t=0
for i in range(N-1):
    if t==1:
        break
    for j in range(i,N):
        if length[i]==length[j]:
            p=0
            l=length[i]
            for k in range(l):
                if password[i][k]!=password[j][l-1-k]:
                    p=1
                    break
            if p==0:
                t=1
                a=l//2
                answer=password[i][a]
                break
print(l,answer)