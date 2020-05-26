S=input()
h=0
s=0
for i in range(len(S)):
    if S[i]==':':
        if S[i+1]=='-':
            if S[i+2]==')':
                h+=1
            elif S[i+2]=='(':
                s+=1
if h==s and h!=0:
    print('unsure')
elif h>s:
    print('happy')
elif s>h:
    print('sad')
elif h==0 and s==0:
    print('none')
        