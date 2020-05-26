x,y,w,h=map(int,input().split())
a1=abs(w-x)
a2=abs(h-y)
a3=x
a4=y
min1=min(a1,a2,a3,a4)
print(min1)