from collections import deque
from itertools import combinations
# 입력으로 받은 선거팀이 유효한지 확인, 모두 연결되었는지 bfs
def check(not_visit):
    if len(not_visit) == 1:
        return True
    if not not_visit:
        return False
    a = list(not_visit)[0]
    check_queue = deque([a])
    checking = [0]*(N+1)
    checking[a] = 1
    # bfs로 모두 연결되었는지 확인
    while check_queue:
        a = check_queue.popleft()
        for k in graph[a]:
            if k in not_visit and checking[k] == 0:
                check_queue.append(k)
                checking[k] = 1

    for k in not_visit:
        if checking[k] == 0:
            return False
    return True

def comb(N):
    # 팀을 나누는 모든 경우의 수를 구함, 조합으로
    # 최대 N//2개롤 뽑으면 나머지는 다른 팀
    min_people = 99999999
    all_node = set([i for i in range(1, N+1)])
    for c in range(1, N//2+1):
        for visit in combinations([i for i in range(1, N+1)], c):
            not_visit = all_node - set(visit)
            current = 0
            for i in visit:
                current += people[i]
            if min_people > abs(current - (all_people - current)):
                # 최솟값이 더 작아지면 두 팀 모두 유효한지 확인
                if check(not_visit) and check(visit):
                    min_people = abs(current - (all_people - current))
    if min_people == 99999999:
        min_people = -1
    return min_people

N = int(input())
people = [0] + list(map(int, input().split()))
graph = {}
all_people = sum(people)
for i in range(1, N+1):
    graph[i] = []
for i in range(1, N+1):
    node = list(map(int, input().split()))
    for j in range(1, node[0]+1):
        graph[i].append(node[j])
print(comb(N))

