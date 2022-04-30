global score
N = int(input())

'''
t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
'''
cmd = []
for i in range(N):
    t, y, x = map(int, input().split())
    cmd.append([t-1, y, x])

green_board = [[0 for col in range(4)] for row in range(6)]
blue_board = [[0 for col in range(4)] for row in range(6)]
red_board = [[0 for col in range(4)] for row in range(4)]

'''
!!WARNING!!
사라진 행, 열 수만큼 움직 
'''

type = [[0, 0], [0, 1], [1, 0]]
score = 0

def convert(pos):
    ret = []
    for y, x in pos:
        ret.append([x, 4-y-1])
    return ret

def is_valid(y, x, board):
    return 0 <= y < 6 and 0 <= x < 4 and board[y][x] == 0

def shoot(pos, board):
    max_move = [0] * len(pos)
    for idx, [y, x] in enumerate(pos):
        for i in range(6):
            if board[i][x] == 1:
                break
            max_move[idx] = max(max_move[idx], i)
    
    min_move = min(max_move)
    
    for y, x in pos:
        board[min_move][x] = 1
    
    # 세로
    if len(pos) == 2 and pos[0][1] == pos[1][1]:
        board[min_move-1][pos[0][1]] = 1

def remove(row, board):
    for j in range(4):
        board[row][j] = 0
    
    for i in range(row, 0, -1):
        for j in range(4):
            board[i][j] = board[i-1][j]

    for j in range(4):
        board[0][j] = 0

def row_check(board):
    global score
    cnt = 0
    for i in range(5, 1, -1):
        if sum(board[i]) == 4:
            cnt += 1
            score += 1
            remove(i, board)
            break
    
    if cnt == 0:
        return False
    return True
    

def overflow_check(board):
    cnt = 0
    if sum(board[1]) > 0:
        cnt += 1
        if sum(board[0]) > 0:
            cnt += 1
    
    for i in range(cnt):
        remove(5, board)

'''
행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다. 
이 경우에는 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후, 
연한 칸에 블록이 있는 경우를 처리해야 한다.
'''

for t, yy, xx in cmd:
    pos = []
    pos.append([yy, xx])
    if t != 0:
        pos.append([yy+type[t][0], xx+type[t][1]])
    shoot(pos, green_board)
    while 1:
        if row_check(green_board) == False:
            break
    overflow_check(green_board)
    pos = convert(pos)
    shoot(pos, blue_board)
    while 1:
        if row_check(blue_board) == False:
            break
    overflow_check(blue_board)

# for i in range(6):
#     print(blue_board[i])

# print("###")

# for i in range(6):
#     print(green_board[i])
    

ans = 0
for i in range(6):
    ans += (sum(green_board[i]) + sum(blue_board[i]))

print(score)
print(ans)