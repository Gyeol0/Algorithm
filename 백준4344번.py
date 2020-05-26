C=int(input())
for _ in range(C):
    A=list(map(int,input().split()))
    m=sum(A[1:])/A[0]
    count=0
    for i in A[1:]:
        if i>m:
            count+=1
    answer=count/A[0]*100
    print('%.3f'%answer+'%')