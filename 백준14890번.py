def Count(arr_1, N, L): # 갈 수 있는 길인지 확인
    s = 1  # 슬로프를 설치할 수 있는지 확인할 연속된 길의 개수
    down = False # 내리막길
    height = arr_1[0] # 현재 높이
    for j in range(1, N):
        if down: # 내리막길 일 때
            if s == L: # 슬로프 설치 가능
                s = 0 # 초기화
                height = arr_1[j] # 높이 재조정
                down = False # 내리막길 아님

            else: # 연속된 길인가
                if height == arr_1[j]:
                    s += 1
                    # 슬로프 설치 가능?
                    if s == L:
                        down = False
                        s = 0
                else:
                    return False
        else:
            # 높이가 1 넘게 차이 나면 불가능
            if abs(height - arr_1[j]) > 1:
                return False
            # 내리막길
            elif height - arr_1[j] == 1:
                down = True
                s = 1
                height = arr_1[j]
                if s == L:
                    s = 0
                    down = False
            # 오르막길
            elif height - arr_1[j] == -1:
                if s >= L: # 현재까지 연속된 길이 L 이상이면 설치가능
                    height = arr_1[j]
                    s = 1
                    down = False
                else:
                    return False
            else:
                s += 1
    # 마지막 끝나고, 내리막길이었는데 연속된 길이 L이었으면 설치, 아니면 불가능(길이 부족함)
    if down:
        if s == L:
            return True
        else:
            return False
    return True
def Slope(N, L, arr, arr_r):
    count = 0
    for i in range(N):
        # 행검사
        if Count(arr[i], N, L):
            count += 1
        # 열검사
        if Count(arr_r[i], N, L):
            count += 1
    return count

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 2차원 행렬 반전
arr_r = list(map(list, zip(*arr)))
print(Slope(N, L, arr, arr_r))