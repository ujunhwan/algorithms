N, M = map(int, input().split())
board = [[0 for col in range(N)] for row in range(N)]
cmd = [[] for _ in range(M)]
cloud_board = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
for i in range(M):
    d, s = map(int, input().split())
    cmd[i] = [d-1, s]

# left, up_left, up, up_right, right, down_right, down, down_left
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

# init
cloud_board[N-1][0] = 1
cloud_board[N-1][1] = 1
cloud_board[N-2][0] = 1
cloud_board[N-2][1] = 1

for idx in range(M):
    # move
    lazy_cloud = [[0 for col in range(N)] for row in range(N)]
    lazy = [[0 for col in range(N)] for row in range(N)]
    is_disappear = [[False for col in range(N)] for row in range(N)]
    is_increase = [[False for col in range(N)] for row in range(N)]
    for i in range(N):
        for j in range(N):
            if cloud_board[i][j] > 0:
                d, s = cmd[idx]
                ny, nx = (i + dy[d]*s + N) % N, (j + dx[d]*s + N) % N
                lazy_cloud[ny][nx] = 1

    for i in range(N):
        for j in range(N):
            cloud_board[i][j] = lazy_cloud[i][j]

    # increase water
    for i in range(N):
        for j in range(N):
            if cloud_board[i][j] > 0:
                is_increase[i][j] = True
                board[i][j] += 1

    # disappear
    for i in range(N):
        for j in range(N):
            if cloud_board[i][j] > 0:
                is_disappear[i][j] = True
            cloud_board[i][j] = 0

    # magic
    for i in range(N):
        for j in range(N):
            if is_increase[i][j]:
                cnt = 0
                for dir in [1, 3, 5, 7]:
                    ny, nx = i + dy[dir], j + dx[dir]
                    if is_valid(ny, nx) and board[ny][nx] > 0:
                        cnt += 1
                
                lazy[i][j] += cnt

    for i in range(N):
        for j in range(N):
            board[i][j] += lazy[i][j]
            lazy[i][j] = 0

    # cloud
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and is_disappear[i][j] == False:
                cloud_board[i][j] = 1
                board[i][j] -= 2

ans = 0
for i in range(N):
    ans += sum(board[i])

print(ans)