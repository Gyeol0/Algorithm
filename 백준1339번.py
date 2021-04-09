def word(s):
    alpha = {}
    # 모든 알파벳이 1이라고 생각하고 알파벳이 위치한 자리 수에 맞게 수를 넣어줌
    # 알파벳마다 수의 합을 딕셔너리에 넣어줌
    for w in s:
        for i in range(len(w)):
            if w[i] not in alpha:
                alpha[w[i]] = 10 ** (len(w) - i -1)
            else:
                alpha[w[i]] += 10 ** (len(w) - i - 1)
    # 내림차순 정렬 후, 높은 수부터 9, 8, 7 ... 곱해서 더해줌
    alpha_sort = sorted(alpha, key = lambda x: alpha[x], reverse = True)
    num = 9
    result = 0
    for i in alpha_sort:
        result += alpha[i] * num
        num -= 1
    return result

N = int(input())
s = [input() for _ in range(N)]
print(word(s))