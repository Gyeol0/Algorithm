def solve():
    A=[]
    for j in range(1,9999):
        
        if j>=1000:
                a1=j//1000
                a2=(j%1000)//100
                a3=((j%1000)%100)//10
                a4=((j%1000)%100)%10
                k=j+a1+a2+a3+a4
        elif j>=100:
                a2=j//100
                a3=(j%100)//10
                a4=(j%100)%10
                k=j+a2+a3+a4
        elif j>=10:
                a3=j//10
                a4=j%10
                k=j+a3+a4        
        else:
                a5=j
                k=j+a5
       
        A.append(k)
        
        
    
    return A 
P=solve()
for i in range(1,9999):
    if i not in P:
        print(i)