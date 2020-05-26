A=int(input())
B=int(input())
C=int(input())
S=A*B*C
li=list(str(S))
answer=[0,0,0,0,0,0,0,0,0,0]
for i in li:
    answer[int(i)]+=1
for i in range(10):
    print(answer[i])