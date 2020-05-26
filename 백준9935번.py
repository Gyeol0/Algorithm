S=input()
boom=input()
l=len(boom)
stack=[]
for i in S:
    stack.append(i)
    if len(stack)>=l:
        a=0
        for j in range(-1,-l-1,-1):
            if stack[j]!=boom[j]:
                a=1
                break
        if a==0:
            k=0
            while k<l:
                stack.pop()
                k+=1
if len(stack)==0:
    print('FRULA')
else:
    ans=''
    for i in stack:
        ans+=i
    print(ans)