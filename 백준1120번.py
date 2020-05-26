A,B=input().split()
lenA=len(A)
lenB=len(B)
if lenA==lenB:
    answer=0
    for i in range(lenA):
        if A[i]!=B[i]:
            answer+=1
else:
    max1=0
    for i in range(lenB-lenA+1):
        sum1=0
        for j in range(lenA):
            if A[j]==B[i+j]:
                sum1+=1
        if sum1>max1:
            max1=sum1
    answer=lenA-max1
print(answer)