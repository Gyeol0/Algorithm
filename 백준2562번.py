for i in range(1,10):
    a=int(input())
    if i==1:
        max1=a
        index1=i
    else:
        if max1<a:
            max1=a
            index1=i
print(max1)
print(index1)