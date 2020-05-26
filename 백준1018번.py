N,M=input().split()
N=int(N)
M=int(M)
A=[0 for i in range(N)]
for i in range(N):
    A[i]=input()
count1=0
count2=0
count3=100000

for k in range(M-7):
    for q in range(N-7):
        count1=0
        count2=0
        for i in range(q,q+8): ###첫번째 W일때
            for j in range(k,k+8):
                if i%2==0 and j%2==0:
                    if A[i][j]!='W':
                        count1+=1
                elif i%2==0 and j%2!=0:
                    if A[i][j]!='B':
                        count1+=1
                elif i%2!=0 and j%2==0:
                    if A[i][j]!='B':
                        count1+=1
                elif i%2!=0 and j%2!=0:
                    if A[i][j]!='W':
                        count1+=1
        count3=min(count1,count3)
        for i in range(q,q+8):##첫번째 B일때
            for j in range(k,k+8):
                if i%2==0 and j%2==0:
                    if A[i][j]!='B':
                        count2+=1
                elif i%2==0 and j%2!=0:
                    if A[i][j]!='W':
                        count2+=1
                elif i%2!=0 and j%2==0:
                    if A[i][j]!='W':
                        count2+=1
                elif i%2!=0 and j%2!=0:
                    if A[i][j]!='B':
                        count2+=1
        count3=min(count2,count3)
print(count3)