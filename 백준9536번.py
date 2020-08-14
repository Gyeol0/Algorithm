T=int(input())
for _ in range(T):
    sound=list(input().split())
    animal=[]
    while True:
        s=list(input().split())
        if s[-1][-1]!='?':
            for i in range(len(sound)):
                if sound[i]==s[-1]:
                    sound[i]=0
        else:
            fox=''
            for i in range(len(sound)):
                if sound[i]!=0:
                    fox+=sound[i]
                    fox+=' '
            break
    print(fox)