def cal(s):
    # -를 기준으로 나눠주고 나머지 모두 괄호를 씌워준다
    s_split = s.split('-')
    num = []
    for i in s_split:
        # 괄호이므로 안에 있는 모든 수를 더해서 append
        split_plus = i.split('+')
        result = 0
        for j in split_plus:
            result += int(j)
        num.append(result)
    # 들어온 수들을 처음 수에서 차례로 빼기
    answer = num[0]
    for i in range(1, len(num)):
        answer -= num[i]
    return answer

s = input()
print(cal(s))