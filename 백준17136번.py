def Change(arr, r, k, x, y): # 한 변이 k인 정사각형을 r로 바꿈
    for i in range(k):
        for j in range(k):
            arr[x+i][y+j] = r
    return arr

def Checking(arr, r, k, x, y): # 한 변이 k인 정사각형이 모두 r인지 확인
    if x + k -1 >= 10 or y + k -1 >= 10:
        return False
    for i in range(k):
        for j in range(k):
            if arr[x+i][y+j] != r:
                return False
    return True

# 밑으로 먼저 간다.
def Paper(x, y, result, arr):
    global min_result
    # 현재 값이 최솟값보다 크면 중단
    if min_result <= result:
        return
    # 맨 밑에 도달하면 오른쪽 맨 위로 이동해서 다시 탐색
    if x == 10:
        Paper(0, y+1, result, arr)
        return
    # 맨오른쪽을 넘어가면 전체 탐색이 끝났으므로 최솟값 비교
    if y == 10:
        min_result = min(result, min_result)
        return

    # 현재 칸이 1인지
    if arr[x][y] == 1:
        # 붙일 색종이
        for k in range(1, 6):
            # 색종이가 남아 있는지
           if count[k] > 0:
               # 색종이를 붙일 수 있는지 확인
                if Checking(arr, 1, k, x, y):
                    # 색종이 붙이고
                    arr = Change(arr, 0, k, x, y)
                    # 색종이 감소
                    count[k] -= 1
                    # 색종이 다음 밑에 칸으로 재귀
                    Paper(x + k, y, result + 1, arr)
                    # 다시 되돌림
                    arr = Change(arr, 1, k, x, y)
                    count[k] += 1
                # 색종이를 못붙임, 작은 색종이를 못붙이면 큰 색종이는 무조건 못붙인다.
                else:
                    return
    # 현재 칸이 0이면 밑에 다음 칸으로 재귀
    else:
        Paper(x + 1, y, result, arr)

count = [5] * 6
min_result = 100
arr = [list(map(int, input().split())) for _ in range(10)]
Paper(0, 0, 0, arr)
if min_result == 100:
    min_result = -1
print(min_result)