global ans
N, M = map(int, input().split())

board = [[0 for col in range(N)] for row in range(N)]
number_board = [[0 for col in range(N)] for row in range(N)]

# number_pos[i] = i번을 가진 블락의 위치 shark = 0
number_pos = [0 for _ in range(N*N)]

for i in range(N):
    board[i] = list(map(int, input().split()))

cmd = [[] for _ in range(M)]
for i in range(M):
    d, s = map(int, input().split())
    cmd[i] = [d-1, s]

# up down left right
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = 0

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

def move():
    stack = 0
    for i in range(0, N*N):
        pos = number_pos[i]
        y, x = pos // N, pos % N
        if board[y][x] == 0:
            stack += 1
        elif stack > 0:
            npos = number_pos[i-stack]
            zy, zx = npos // N, npos % N
            # swap
            tmp = board[y][x]
            board[y][x] = board[zy][zx]
            board[zy][zx] = tmp

def explode():
    global ans
    stack = 0
    prev_val = 0
    boom = False
    for i in range(0, N*N):
        pos = number_pos[i]
        y, x = pos // N, pos % N
        val = board[y][x]
        if val == 4: continue

        if val == 0:
            if stack >= 4:
                # i-stack ~ i-1 boom
                boom = True
                for j in range(i-stack, i):
                    boom_pos = number_pos[j]
                    by, bx = boom_pos // N, boom_pos % N
                    board[by][bx] = 0
                ans += (stack) * prev_val
            stack = 0
            break

        else:
            if prev_val == val:
                stack += 1
            else:
                if stack >= 4:
                    # i-stack ~ i-1 boom
                    boom = True
                    for j in range(i-stack, i):
                        boom_pos = number_pos[j]
                        by, bx = boom_pos // N, boom_pos % N
                        board[by][bx] = 0
                    ans += (stack) * prev_val
                    
                prev_val = val
                stack = 1
    
    # if stack left
    if stack >= 4:
        boom = True
        for j in range(N*N-1-stack, N*N):
            boom_pos = number_pos[j]
            by, bx = boom_pos // N, boom_pos % N
            board[by][bx] = 0
        ans += (stack) * prev_val
    
    return boom

def change():
    # lazy = [0 for _ in range(N*N)]
    # lazy[0] = 4
    lazy = [4]
    prev_val = -1
    stack = 0
    # idx = 1
    for i in range(N*N):
        pos = number_pos[i]
        y, x = pos // N, pos % N
        val = board[y][x]
        if val == 4: continue
        if val == 0:
            if stack > 0:
                lazy.append(stack)
                lazy.append(prev_val)

            stack = 0
            break
        else:
            if prev_val == val:
                stack += 1
            else:
                if stack > 0:
                    lazy.append(stack)
                    lazy.append(prev_val)
            
                prev_val = val
                stack = 1
    
    if stack > 0:
        lazy.append(stack)
        lazy.append(prev_val)

    for i in range(N):
        for j in range(N):
            board[i][j] = 0

    length = min(N*N, len(lazy))
    for i in range(length):
        pos = number_pos[i]
        y, x = pos // N, pos % N
        board[y][x] = lazy[i]

# initial number setting
length, val = 1, 1
y, x = (N-1)//2, (N-1)//2
cnt = 0
is_possible = True
while is_possible:
    for dir in [2, 1, 3, 0]:
        cnt = (cnt + 1) % 2
        for i in range(length):
            ny, nx = y + dy[dir], x + dx[dir]
            if not is_valid(ny, nx) or number_board[ny][nx] > 0:
                is_possible = False
                break
            number_board[ny][nx] = val
            val += 1
            y, x = ny, nx
        if cnt & 1 == 0:
            length += 1

for i in range(N):
    for j in range(N):
        number_pos[number_board[i][j]] = i*N+j

# set shark position
sy, sx = (N-1)//2, (N-1)//2
board[sy][sx] = 4

# blizzard
for d, s in cmd:
    for distance in range(1, s+1):
        y, x = sy + dy[d]*distance, sx + dx[d]*distance
        board[y][x] = 0

    while 1:
        move()
        if not explode():
            break
    change()

    # for i in range(N):
    #     print(board[i])
    # print("------")

print(ans)

'''
3 1
1 0 1
0 0 0
1 0 1
1 1
'''