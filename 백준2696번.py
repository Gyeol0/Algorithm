import heapq
import sys
def Middle(M, arr, count):
    # 중앙값보다 큰 값, 최솟값이 중앙값보다 커야 한다. 중앙값보다 작으면 small_heap에 push, 오름차순 정렬
    big_heap = []
    # 중앙값보다 작은 값, 내림차순 정렬
    small_heap =[]
    # 필요 개수만큼 배열 초기화
    answer = [0]*count
    # 무조건 작은 힙의 길이가 1 더 길거나 큰 힙과 같다.
    
    # 1. 두 힙의 길이가 같을 때에는 중앙값보다 큰 힙의 최솟값과 새로운 값을 비교
    # 새로운 값이 더 크면 큰 힙에서 최솟값 pop, 새로운 값 push, pop한 값을 중앙값보다 작은 힙에 push
    # 새로운 값이 더 작거나 같으면 작은 힙에 push
    # 둘 다 비어 있으면 작은 힙에 push
    # 작은 힙의 최댓값이 중앙값
    # 이 떄가 홀수번 째 수이므로 작은 힙의 최댓값을 출력
    
    # 2. 두 힙의 길이가 다를 떄, 작은 힙의 최댓값과 새로운 값을 비교
    # 새로운 값이 더 크거나 같으면 큰 힙에 push
    # 새로운 값이 더 작으면 작은 힙의 최댓값은 pop, 새로운 값 push, pop한 값을 큰 힙에 push
    for i in range(M):
        # 1. 길이가 같음
        if len(big_heap) == len(small_heap):
            # 둘 다 비어 있으면 작은 힙에 push
            if not small_heap:
                heapq.heappush(small_heap, (-arr[i], arr[i]))
            else:
                a = big_heap[0]
                # 새로운 값이 더 작음
                if a >= arr[i]:
                    heapq.heappush(small_heap, (-arr[i], arr[i]))
                
                # 새로운 값이 더 커서 바꿔줌
                else:  
                    heapq.heappush(small_heap, (-a, a))
                    heapq.heappop(big_heap)
                    heapq.heappush(big_heap, arr[i])
            # 중앙값
            answer[i // 2] = small_heap[0][1]
        # 2. 길이가 다름
        else:
            a = small_heap[0][1]
            # 새로운 값이 크거나 같음
            if arr[i] >= a:
                # 큰 힙에 push
                heapq.heappush(big_heap, arr[i])
            
            # 새로운 값이 더 작아서 바꿔줌
            else:
                heapq.heappop(small_heap)
                heapq.heappush(small_heap, (-arr[i], arr[i]))
                heapq.heappush(big_heap, a)
    return answer

## 밑에는 그냥 10개씩 출력하는거 볼 필요 없음
T = int(input())
for t in range(T):
    M = int(input())
    if M % 10:
        line = M // 10 + 1
    else:
        line = M // 10

    if M % 2:
        count = M // 2 + 1
    else:
        count = M // 2
    print(count)
    arr = []
    for k in range(line):
        arr1 = list(map(int, sys.stdin.readline().split()))
        arr.extend(arr1)
    answer = Middle(M, arr, count)
    if count % 10:
        line2 = count // 10 + 1
    else:
        line2 = count // 10
    for l in range(1, line2 + 1):
        print(*answer[(l-1)*10: l*10])