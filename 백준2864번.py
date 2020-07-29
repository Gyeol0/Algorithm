A,B=input().split()
A=list(A)
B=list(B)
num1=''
num2=''
for i in range(len(A)): #5를 모두 6으로 변경
    if A[i]=='5':
        A[i]='6'
    if B[i]=='5':
        B[i]='6'
for i in range(len(A)):
    num1+=A[i]
    num2+=B[i]
    
max_num=int(num1)+int(num2) #최대
num1=''
num2=''
for i in range(len(A)): #6을 모두 5로 변경
    if A[i]=='6':
        A[i]='5'
    if B[i]=='6':
        B[i]='5'
for i in range(len(A)):
    num1+=A[i]
    num2+=B[i]
    
min_num=int(num1)+int(num2) #최소

print(min_num, max_num)