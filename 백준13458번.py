def Exam(room, B, C):
    count = 0
    for i in room:
        # 총감독관 1명
        count += 1
        k = i - B
        # 나머지 인원 감독
        if k > 0:
            if k % C == 0:
                count += k // C
            else:
                count += k // C + 1
    return count

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
print(Exam(A, B, C))