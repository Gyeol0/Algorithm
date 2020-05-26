import sys
lines=sys.stdin.read()
alph=['a','b','c','d','e','f','g','h','i','j','k',
      'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
length=len(alph)
count=[0 for i in range(len(alph))]
for i in lines:
    for j in range(length):
        if i==alph[j]:
            count[j]+=1
            break
max1=max(count)
answer=''
for i in range(length):
    if max1==count[i]:
        answer+=alph[i]
print(answer)
    