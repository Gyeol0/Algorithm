n=int(input())
li=[0 for _ in range(n)]
for i in range(n):
    li[i]=int(input())
li.sort()
for i in range(n):
    print(li[i])