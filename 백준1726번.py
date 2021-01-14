G=int(input())
answer=[]
l=[1,2]
k=3
while l[-1]**2-l[-2]**2<=G:
    l.append(k)
    k+=1
for i in range(len(l)-1,0,-1):
    for j in range(i-1,-1,-1):
        if l[i]**2-l[j]**2==G:
            answer.append(l[i])
            break
        elif l[i]**2-l[j]**2>G:
            break
answer.sort()
if len(answer)==0:
    print(-1)
else:
    for i in answer:
        print(i)