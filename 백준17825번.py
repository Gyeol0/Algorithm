def changeType(current_type, current):
    if current_type == 1:
        if current == 5:
            current_type = 2
            current = 0
        elif current == 10:
            current_type = 3
            current = 0
        elif current == 15:
            current_type = 4
            current = 0
    return current_type, current

def dfs(idx, result, visit, arr, piece):
    global max_result
    if idx == 10:
        if max_result < result:
            max_result = result
        return

    for j in range(1,5):
        if piece[j] != 'end':
            current_type = piece[j][0]
            current = piece[j][1]
            if current + arr[idx] < max_type[current_type]:
                new_result = result + board[current_type][current+arr[idx]]
                new_type, new_current = changeType(current_type, current + arr[idx])
                flag = False
                for k in range(1, 5):
                    if j != k and piece[k] != 'end':
                        if piece[k][0] == new_type and piece[k][1] == new_current:
                            flag = True
                            break
                        if board[piece[k][0]][piece[k][1]] == 25 and board[new_type][new_current] == 25:
                            flag = True
                            break
                        if board[piece[k][0]][piece[k][1]] == 40 and board[new_type][new_current] == 40:
                            flag = True
                            break
                        if board[piece[k][0]][piece[k][1]] == 10 and board[new_type][new_current] == 10:
                            flag = True
                            break
                        if board[piece[k][0]][piece[k][1]] == 30 and board[new_type][new_current] == 30:
                            if (piece[k][0],piece[k][1],new_type,new_current) in over_type:
                                flag = True
                                break
                        if board[piece[k][0]][piece[k][1]] == 35 and board[new_type][new_current] == 35:
                            flag = True
                            break

                if flag:
                    continue
                else:
                    piece[j] = [new_type, new_current]
                    dfs(idx + 1, new_result,visit, arr, piece)
                    piece[j] = [current_type, current]
            else:
                piece[j] = 'end'
                dfs(idx+1, result, visit, arr, piece)
                piece[j] = [current_type, current]

type1 = [0] * 21
for i in range(21):
    type1[i] = i*2
type2 = [10, 13, 16, 19, 25, 30, 35, 40]
type3 = [20, 22, 24, 25, 30, 35, 40]
type4 = [30, 28, 27, 26, 25, 30, 35, 40]
max_type = [0, 21, 8, 7, 8]
board = [0, type1, type2, type3, type4]
piece = [[1, 0] for _ in range(5)]
arr = list(map(int, input().split()))
visit = [0]*10
over_type = [(1,15,4,0), (4,0,1,15),(2,5,3,4),(3,4,2,5),(2,5,4,5),(4,5,2,5),(3,4,4,5),(4,5,3,4)]
max_result = 0
dfs(0, 0, visit, arr,piece)
print(max_result)