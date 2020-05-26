R,B=map(int,input().split())
S=R+B
t=0
for i in range(2,5000):
    for j in range(2,5000):
        if 2*i+2*j-4==R:
            if i*j==S:
                t=1
                
                answer=[i,j]
                break
    if t==1:
        break
if answer[1]>answer[0]:
    print(answer[1],answer[0])
else:
    print(answer[0],answer[1])