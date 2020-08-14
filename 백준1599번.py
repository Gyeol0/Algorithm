alp=['a','b','k','d','e','g','h','i','l','m','n','c','o','p','r','s','t','u','w','y']
N=int(input())
ch=[]
ch_1=[]
for _ in range(N):
    ch.append(input())
for i in range(N):
    ch[i]=ch[i].replace('ng','c')
for i in range(N-1):
    for j in range(i+1,N):
        a1=ch[i]
        a2=ch[j]
        len1=len(a1)
        len2=len(a2)
        first=0
        for k in range(min(len1,len2)):
            if a1[k]!=a2[k]:
                idx1=alp.index(a1[k])
                idx2=alp.index(a2[k])
                if idx1>idx2:
                    first=2
                else:
                    first=1
                break
        if first==0:
            if len1>len2:
                first=2
            else:
                first=1
        if first==2:
            ch[i],ch[j]=ch[j],ch[i]
for i in range(N):
    ch[i]=ch[i].replace('c','ng')
        
for i in range(N):
    print(ch[i])