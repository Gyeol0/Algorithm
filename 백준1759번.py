from itertools import combinations
def password(L, s):
    # 조합 생성
    com = list(combinations(s, L))
    answer = []
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in com:
        count = 0
        word = []
        # 증가하는 순으로 만들기 위해서
        for j in sorted(i):
            # 모음 확인
            if j in vowel:
                count += 1
            word.append(j)
        # 모음 최소 1개, 자음 최소 2개
        if count >= 1 and len(word) - count >= 2:
            answer.append(''.join(word))
    return sorted(answer)

L, C = map(int, input().split())
s = input().split()
answer = password(L, s)
for i in answer:
    print(i)