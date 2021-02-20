def Stairs(N, stair):
    # 계단이 1개
    if N == 1:
        return stair[0]
    # 계단이 2개
    elif N == 2:
        return stair[1] + stair[0]
    arr = []
    arr.append(stair[0])
    arr.append(stair[0] + stair[1])
    arr.append(max(stair[1] + stair[2], stair[0] + stair[2]))
    for i in range(3, N):
        # max(직전 계단을 밟았을 때, 직전 계단을 밟지 않았을 때)
        # 직전 계단을 밟았으면, stair[i-1] + stair[i]에다가 그전에 2칸을 올랐으니까 그때까지 최대인 arr[i-3]
        # 안밟았으면 현재 stair[i]와 2칸 전 최대인 arr[i-2]
        arr.append(max(stair[i-1] + stair[i] + arr[i-3], stair[i] + arr[i-2]))
    return arr[-1]
N = int(input())
stair = [int(input()) for _ in range(N)]
print(Stairs(N, stair))