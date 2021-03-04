def Tiger(D, K):
    # A가 더해진 개수
    A_count = 0
    # B가 더해진 개수
    B_count = 0
    # dp
    arr = []
    arr.append('A')
    arr.append('B')
    for i in range(2, D):
        arr.append(arr[i-1] + arr[i-2])
    # A, B 카운트
    for i in arr[-1]:
        if i == 'A':
            A_count += 1
        else:
            B_count += 1
    # K = A  * A_count + B * B_count
    # 1부터 시작하여 A 탐색, K에서 A개수 * A를 뺀 것이 B 개수로 나누어떨어지는 최솟값
    A = 1
    while (K - A_count * A) % B_count:
        A += 1
    # B 계산
    B = (K - A_count * A) // B_count

    return A, B

D, K = map(int, input().split())
result = Tiger(D, K)
print(result[0])
print(result[1])
