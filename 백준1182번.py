N,S=map(int,input().split())
lst=list(map(int,input().split()))
answer=0
def total(idx,t): #재귀
    global answer
    if idx==N:
        return 
    else:
        if t+lst[idx]==S:
            answer+=1
        total(idx+1,t+lst[idx]) #현재 원소를 부분집합에 포함하는 경우
        total(idx+1,t)  #현재 원소를 부분집합에 포함하지 않는 경우
        
total(0,0)
print(answer)