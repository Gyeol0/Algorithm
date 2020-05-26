n=int(input())
A=[]
for i in range(n):
    A.append(input().split())

    for j in range(len(A[i])):
        A[i][j]=int(A[i][j])


B=[[0]*n for i in range(n)]

for i in range(n):
    for j in range(len(A[i])):
        if j==0:
            B[i][j]=B[i-1][j]+A[i][j]
        elif j==len(A[i])-1:
            B[i][j]=B[i-1][j-1]+A[i][j]
        else:
            B[i][j]=max(B[i-1][j],B[i-1][j-1])+A[i][j]
                   
print(max(B[n-1]))
