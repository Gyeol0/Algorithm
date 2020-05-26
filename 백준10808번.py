S=input()
al=['a','b','c','d','e','f','g',
    'h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u',
    'v','w','x','y','z']
count=[0 for _ in range(26)]
for i in S:
    for j in range(26):
        if i==al[j]:
            count[j]+=1
            break
for i in count:
    print(i,end=' ')