def solution(N, stages):
    answer = []
    ans={}
    for i in range(1,N+1):
        fail=0
        arrive=0
        for j in stages:
            if i<=j:
                arrive+=1
                if i==j:
                    fail+=1
        if arrive==0:
            per=0
        else:
            per=fail/arrive
        ans[i]=per
    answer=sorted(ans,key=lambda x: ans[x],reverse=True)
    return answer