T=int(input())
for _ in range(T):
    H,W,N=map(int,input().split())
    front=N%H
    end=N//H
    if front==0:
        front=str(H)
        if end<10:
            end='0'+str(end)
        else:
            end=str(end)
    else:
        front=str(front)
        if end+1<10:
            end='0'+str(end+1)
        else:
            end=str(end+1)

    answer=front+end
    print(answer)