"""
요세푸스 문제
start 1부터, start + (k - 1)이 제거
제거한 후 start를 제거한 번호로, M보다 제거되는 index가 작으면 M 1 감소, 같을 때에는 종료(죽음)
N도 1 감소
"""
def picnic(N, K, M):
    count = 1
    start = 0
    while True:
        remove = (start + (K - 1)) % N
        if remove == M:
            break
        elif remove < M:
            M -= 1
        start = remove
        N -= 1
        count += 1

    return count


"""
무조건 제거하는 사람을 1번으로 놓고 시작
이제 무조건 K번째 사람이 죽는다.
"""
def picnic2(N, K, M):
    count = 1
    while True:
        # K가 더 크면 나머지로, 나머지가 0이면 맨끝이니까 N으로 바꿔주고
        if K > N:
            k = K % N
            if k == 0:
                k = N
        else:
            k = K

        if k == M:
            break
        if M - k > 0:
            M = M - k
        elif M - k < 0:
            M = M - k + N
        N -= 1
        count += 1

    return count
N, K, M = map(int, input().split())
print(picnic2(N, K, M))