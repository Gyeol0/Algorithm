A=input()
count=0
K=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in K:
    while i in A:
        length=len(i)
        index1=A.index(i)
        
        A=A.replace(i,' ',1)
        count+=1
while ' ' in A:
    A=A.replace(' ','')
answer=count+len(A)
print(answer)