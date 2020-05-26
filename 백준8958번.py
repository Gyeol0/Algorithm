T=int(input())
for i in range(T):
    A=list(input())
    l=len(A)
    count=0
    S=0
    answer=[]
    for j in range(l):
        if A[j]=='O':
            count+=1
            if j==l-1:
                answer.append(count)
        else:
            answer.append(count)
            count=0
    for j in answer:
        s=0
        for k in range(1,j+1):
           s+=k
        S+=s
    print(S)