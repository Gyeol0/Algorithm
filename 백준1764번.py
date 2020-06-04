N,M=map(int,input().split())
A=[]
B=[]
answer=[]
for _ in range(N):
    A.append(input())
for _ in range(M):
    B.append(input())
    
    
answer=list(set(A)&set(B))
answer.sort()
print(len(answer))
for i in answer:
    print(i)