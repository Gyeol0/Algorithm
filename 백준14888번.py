import itertools
n=int(input())
num=list(map(int,input().split()))
cal=list(map(int,input().split()))
cal_lst=[]
max_num=-1000000000 #최대 지정
min_num=1000000000 #최솟 지정
for i in range(len(cal)):
    for j in range(cal[i]):
        cal_lst.append(i)
all_cal=list(set(list(itertools.permutations(cal_lst,len(cal_lst))))) #연산자 배열 경우의 수
for i in all_cal: #연산자에 따른 계산
    answer=num[0]
    for j in range(len(i)):
        if i[j]==0:
            answer=answer+num[j+1]
        elif i[j]==1:
            answer=answer-num[j+1]
        elif i[j]==2:
            answer=answer*num[j+1]
        else:
            if answer<0:
                answer=(-answer)//num[j+1]*(-1)
            else:
                answer=answer//num[j+1]
    if answer>max_num:
        max_num=answer
    if answer<min_num:
        min_num=answer
print(max_num)
print(min_num)