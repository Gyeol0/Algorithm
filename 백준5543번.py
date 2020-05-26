A=[]
B=[]
min1=999999
for _ in range(3):
    A.append(int(input()))
for _ in range(2):
    B.append(int(input()))
for i in range(3):
    for j in range(2):
        S=A[i]+B[j]-50
        if min1>S:
            min1=S
print(min1)