# Union-find
def findParent(x):
   if parent[x] == x:
       return x
   p = findParent(parent[x])
   parent[x]=p
   return parent[x]

def unionParent(x,y):
    x = findParent(x)
    y = findParent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]
parent = {i:i for i in range(0,g+1)}
result = 0
for plane in planes:
    x = findParent(plane)
    if x == 0:
        break
    unionParent(x, x-1)
    result += 1
print(result)