def solution(n, k):
    import math
    A=[]
    for i in range(1,n+1):
        A.append(i)
    answer = []
    for i in range(1,n+1):
        fac=math.factorial(n-i)
        start=int(k/fac)
        if k%fac==0:
            start=start-1
        answer.append(A[start])
        del A[start]
        k=k%fac
        if k==1:
            answer.extend(A)
            break
    return answer
import math
n=int(input())
li=list(map(int,input().split()))
B=[i for i in range(1,n+1)]
if li[0]==1:
    a=solution(n,li[1])
    for i in a:
        print(i, end=' ')
elif li[0]==2:
    count=0
    for i in range(1,n+1):
        fac=math.factorial(n-i)
        index1=B.index(li[i])
        count=count+index1*fac
        del B[index1]
    count+=1
    print(count)
        