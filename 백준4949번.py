while True:
    S=input()
    if S=='.':
        break
    t1=0
    t2=0
    c=0
    k=[]
    for i in S:
        if i=='(':
            t1+=1
            k.append(1)
        elif i=='[':
            t2+=1
            k.append(2)
        elif i==')':
            if t1>0:
                p=k.pop()
                if p==1:
                    t1-=1
                else:
                    c=1
                    break
            else:
                c=1
                break

        elif i==']':
            if t2>0:
                p=k.pop()
                if p==2:
                    t2-=1
                else:
                    c=1
                    break
            else:
                c=1
                break
    if c==1 or t1>0 or t2>0:
        print('no')
    elif t1==0 and t2==0:
        print('yes')