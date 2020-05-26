def min(a,b,c=100000):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else:
        return c
def one():
    k=int(input())
    li=[]
    li.append(0)
    li.append(0)
    li.append(1)
    li.append(1)
    for i in range(4,k+1):
        if i%3==0 and i%2==0:
            li.append(min(li[int(i/3)],li[int(i/2)],li[i-1])+1)
        elif i%3==0 and i%2!=0:
            li.append(min(li[int(i/3)],li[int(i-1)])+1)
        elif i%3!=0 and i%2==0:
            li.append(min(li[int(i/2)],li[int(i-1)])+1)
        else:
            li.append(li[i-1]+1)
          
    print(li[k])

one()
                  
