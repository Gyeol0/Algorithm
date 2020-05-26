S=input()
A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
B=[-1 for i in range(len(A))]
for i in range(len(S)):
    index1=A.index(S[i])
    if B[index1]==-1:
        B[index1]=i
    
for i in range(len(B)):
    print(B[i], end=' ')