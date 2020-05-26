A=[]
for _ in range(5):
    A.append(int(input()))
    if A[-1]<=40:
        A[-1]=40
print(int(sum(A)/len(A)))