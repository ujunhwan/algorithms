'''
1. spread his smell on his own position
2. move every 1 second and spread his smell
3. smells gonna be out after kth move
'''

N, M, K = map(int, input().split())
board = [[0 for col in range(N)] for row in range(N)]
smell = [[0 for col in range(N)] for row in range(N)]
smell_time = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))

# current direction of shark
sharks = [0] + list(map(int, input().split()))

# zero up down left right
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

prior = [[list() for col in range(5)] for row in range(M+1)]

for num in range(1, M+1):
    for i in [1, 2, 3, 4]:
        prior[num][i] = list(map(int, input().split()))

'''
smell -> move -> smell -> move
'''

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

def spread():
    pass

def move(y, x, lazy, lazy_smell):
    num = board[y][x]
    dir = sharks[num]
    
    # search next
    emp = 0
    mine = 0
    ndir = prior[num][dir]
    for k in ndir:
        ny, nx = y + dy[k], x + dx[k]
        if not is_valid(ny, nx): continue
        if smell[ny][nx] == 0:
            emp += 1
        if smell[ny][nx] == num:
            mine += 1

    is_done = False
    if emp > 0:
        for k in ndir:
            ny, nx = y + dy[k], x + dx[k]
            if not is_done and is_valid(ny, nx) and smell[ny][nx] == 0:
                is_done = True
                if (lazy[ny][nx] == 0) or (lazy[ny][nx] > num):
                    lazy[ny][nx] = num
                    lazy_smell[ny][nx] = num
                    sharks[num] = k
    else:
        for k in ndir:
            ny, nx = y + dy[k], x + dx[k]
            if not is_done and is_valid(ny, nx) and smell[ny][nx] == num:
                is_done = True
                if (lazy[ny][nx] == 0) or (lazy[ny][nx] > num):
                    lazy[ny][nx] = num
                    lazy_smell[ny][nx] = num
                    sharks[num] = k

def out():
    pass

# first smell out
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            smell[i][j] = board[i][j]
            smell_time[i][j] = K

is_done = False
for time in range(1000):
# for time in range(4):
    # init
    lazy = [[0 for col in range(N)] for row in range(N)]
    lazy_smell = [[0 for col in range(N)] for row in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                move(i, j, lazy, lazy_smell)

    # decrease time
    for i in range(N):
        for j in range(N):
            if smell_time[i][j] > 0:
                smell_time[i][j] -= 1
                if smell_time[i][j] == 0:
                    smell[i][j] = 0

    # move
    for i in range(N):
        for j in range(N):
            board[i][j] = lazy[i][j]
            if lazy_smell[i][j] > 0:
                smell[i][j] = lazy_smell[i][j]
                smell_time[i][j] = K
    
    # check
    cand = 0
    for i in range(N):
        cand += sum(board[i])
    if cand == 1:
        print(time+1)
        is_done = True
        break

if not is_done:
    print(-1)