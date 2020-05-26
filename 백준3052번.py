A=[]
for _ in range(10):
    a=int(input())
    A.append(a%42)
A=list(set(A))
print(len(A))