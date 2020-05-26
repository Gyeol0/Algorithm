A,B=input().split()
a=list(A)
a.reverse()
b=list(B)
b.reverse()
a1=''
b1=''
for i in range(3):
    a1+=a[i]
    b1+=b[i]
for i in range(3):
    if a[i]>b[i]:
        print(int(a1))
        break
    elif a[i]<b[i]:
        print(int(b1))
        break