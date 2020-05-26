N=int(input())
if N>0:
    A=list(map(int,input().split()))
    count=0
    for i in A:
        if i==1:
            count+=1
        elif i==2:
            continue
        else:
            for j in range(2,i//2+2):
                if i%j==0:
                    count+=1
                    break
    answer=len(A)-count
else:
    answer=0
    
print(answer)