global shark_move_value, shark_count
M, S = map(int, input().split())
# board = [[] for _ in range(16)]
board = [[0 for col in range(8)] for row in range(16)]
for i in range(M):
    y, x, d = map(int, input().split())
    board[(y-1)*4+(x-1)][d-1] += 1

sy, sx = list(map(int, input().split()))
shark = [sy-1, sx-1]

d8y = [0, -1, -1, -1, 0, 1, 1, 1]
d8x = [-1, -1, 0, 1, 1, 1, 0, -1]

d4y = [-1, 0, 1, 0]
d4x = [0, -1, 0, 1]

# 위치, 시간 [y, x, time]
smell = [[] for col in range(101)]

# 냄새도 체크 
def is_valid(y, x, t):
    sy, sx = shark
    if 0 <= y < 4 and 0 <= x < 4:
        if sy*4+sx == y*4+x:
            return False
        if t == 0:
            return True
        elif t == 1 and y*4+x not in smell[0]:
            return True
        elif (y*4+x not in smell[t-1]) and (y*4+x not in smell[t-2]):
            return True
        return False
    return False

def can_shark_go(y, x):
    return 0 <= y < 4 and 0 <= x < 4

shark_visited = [False for _ in range(16)]
def shark_move(y, x, cnt, move_value):
    global shark_count, shark_move_value

    if move_value > 100:
        if shark_count < cnt:
            shark_count = cnt
            shark_move_value = move_value
        elif shark_count == cnt:
            shark_move_value = min(shark_move_value, move_value)
        return

    for k in range(4):
        ny, nx = y + d4y[k], x + d4x[k]
        if can_shark_go(ny, nx):
            num = 0
            for i in range(8):
                num += board[ny*4+nx][i]
            if shark_visited[ny*4+nx]:
                shark_move(ny, nx, cnt, 10*move_value + (k+1))
            else:
                shark_visited[ny*4+nx] = True
                shark_move(ny, nx, cnt+num, 10*move_value + (k+1))
                shark_visited[ny*4+nx] = False


for time in range(S):
    # init
    shark_count = -1
    shark_move_value = 1000

    # copy
    copy = [[0 for col in range(8)] for row in range(16)]

    for i in range(16):
        for j in range(8):
            copy[i][j] += board[i][j]

    # fish move
    for i in range(16):
        for dir in range(8):
            if copy[i][dir] == 0:
                continue
            y, x = i//4, i%4
            for k in range(8):
                next_dir = (dir-k+8)%8
                ny, nx = y + d8y[next_dir], x + d8x[next_dir]
                if is_valid(ny, nx, time):
                    board[ny*4+nx][next_dir] += copy[i][dir]
                    board[i][dir] -= copy[i][dir]
                    break
    
    # debug = [sum(board[i]) for i in range(16)]
    # print(debug)
    
    # shark 3 times move
    sy, sx = shark
    shark_move(sy, sx, 0, 0)

    for i in range(3):
        dir = shark_move_value // (10**(2-i))
        shark_move_value %= (10**(2-i))
        sny, snx = sy + d4y[dir-1], sx + d4x[dir-1]
        if sum(board[sny*4+snx]) > 0:
            smell[time].append(sny*4+snx)
            for j in range(8):
                board[sny*4+snx][j] = 0
        sy, sx = sny, snx
    
    shark = [sy, sx]

    # 복제완료
    for i in range(16):
        for j in range(8):
            board[i][j] += copy[i][j]

ans = 0
for i in range(16):
    for j in range(8):
        ans += board[i][j]

print(ans)