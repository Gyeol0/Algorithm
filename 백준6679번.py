for i in range(1000,10000):
    a1=i
    a2=i
    a3=i
    s1=0
    s2=0
    s3=0
    while a1!=0:
        s1+=a1%10
        a1=a1//10
    while a2!=0:
        s2+=a2%12
        a2=a2//12
    while a3!=0:
        s3+=a3%16
        a3=a3//16
    if s1==s2 and s2==s3 and s1==s3:
        print(i)