N=int(input())
A=[]
for i in range(10000000000):
    if '666' in str(i):
        A.append(i)
    if len(A)==N:
        break
print(A[N-1])