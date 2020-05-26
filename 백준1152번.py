string=input()
count=0
for i in range(len(string)):
    if string[i]==' ':
        if i==0 or i==len(string)-1:
            continue
        count+=1
        

    
count=count+1
if string==' ':
    count=0

print(count)