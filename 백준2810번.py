N=int(input())
L=list(input())
count=0
check=0
l=len(L)
ch='*'
for i in range(l):
    ch+=L[i]
    if L[i]!='L':
        ch+='*'
    else:
        if check==1:
            ch+='*'
            check=0
        else:
            check+=1
ch=list(ch)
for i in range(len(ch)):
    if ch[i]=='S' or ch[i]=='L':
        if ch[i-1]=='*':
            ch[i-1]=1
            count+=1
            ch[i]=0
        elif ch[i+1]=='*':
            ch[i+1]=1
            ch[i]=0
            count+=1
print(count)