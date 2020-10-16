import itertools
def solution(relation):
    answer = 0
    key=[]
    l=len(relation)
    col=len(relation[0])
    col_list=[i for i in range(col)]
    l=len(relation)
    key_answer=[]
    for i in range(1,col+1):
        com=itertools.combinations(col_list,i)
        for j in com:
            diff=[]
            for k in relation:
                a=[]
                for p in j:
                    a.append(k[p])
                diff.append(a)
            c=0
            for k in range(len(diff)-1):
                for p in range(k+1,len(diff)):
                    if diff[k]==diff[p]:
                        c=1
                        break
                if c==1:
                    break
            if c==0:
                key.append(list(j))

    while key:
        key_1=key.pop(0)
        answer+=1
        k=0
        while k<len(key):
            if set(key_1)==set(key_1).intersection(set(key[k])):
                key.pop(k)
            else:
                k+=1
    return answer