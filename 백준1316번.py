N=int(input())
count=0
for _ in range(N):
    t=input()
    
    for i in range(len(t)-1):
        k=1
        stop=0
        for j in range(i+1,len(t)):
            if k==1 and t[i]==t[j]:
                continue
            elif k==1 and t[i]!=t[j]:
                k=0
            elif k==0 and t[i]==t[j]:
                stop=1
                break
        if stop==1:
            count+=1
            break
answer=N-count
print(answer)