T=int(input())
alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
     'P','Q','R','S','T','U','V','W','X','Y','Z']
for _ in range(T):
    ch1,ch2=input().split()
    ch1=list(ch1)
    ch2=list(ch2)
    l=len(ch1)
    dis=[]
    for i in range(l):
        idx2=alp.index(ch2[i])+1
        idx1=alp.index(ch1[i])+1
        distance=idx2-idx1
        if distance<0:
            distance=distance+26
        dis.append(distance)
    print('Distances:',end=' ')
    for i in dis:
        print(i, end=' ')
    print()