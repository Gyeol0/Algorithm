from itertools import permutations
import sys
# 이닝 마다 점수 계산 함수
def Baseball(innings, array):
    # 현재 타자 순서
    current = 0
    score = 0
    for inning in innings:
        out = 0
        # 1루, 2루, 3루 주자 있는지
        # 배열로 썼더니 시간 초과
        step1, step2, step3 = 0, 0, 0
        while out < 3:
            # 아웃
            if inning[array[current]] == 0:
                out += 1
            # 1루타
            elif inning[array[current]] == 1:
                score += step3
                step3, step2, step1 = step2, step1, 1
            # 2루타
            elif inning[array[current]] == 2:
                score += step3 + step2
                step3, step2, step1 = step1, 1, 0
            # 3루타
            elif inning[array[current]] == 3:
                score += step1 + step2 + step3
                step3, step2, step1 = 1, 0, 0
            # 4루타
            elif inning[array[current]] == 4:
                score += step1 + step2 + step3 + 1
                step3, step2, step1 = 0, 0, 0
            # 0~8 돌고 다시 0부터
            current = (current + 1) % 9
    return score

N = int(sys.stdin.readline())
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_total = 0
# 0 ~ 8 모든 순열
for array in permutations(range(1,9), 8):
    array = list(array[:3]) + [0] + list(array[3:])
    max_total = max(Baseball(innings, array), max_total)
print(max_total)