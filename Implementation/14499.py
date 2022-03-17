# https://www.acmicpc.net/problem/14499
# 14499번 주사위 굴리기

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, Y, X, K = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

cmd = list(map(int, input().split()))

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]

idx_map = [[-1 for col in range(5)] for row in range(5)]
idx_map[0][2] = idx_map[2][0] = idx_map[2][4] = idx_map[4][2] = 1
idx_map[1][2] = 3
idx_map[2][2] = 0
idx_map[2][1] = 4
idx_map[3][2] = 2
idx_map[2][3] = 5

# right 1 left 2 north 3 south 4
def move(direction):
    # dicemap move
    if direction == 0:
        for i in [3, 2, 1]:
            idx_map[2][i] = idx_map[2][i-1]
    elif direction == 1:
        for i in [1, 2, 3]:
            idx_map[2][i] = idx_map[2][i+1]
    elif direction == 2:
        # south
        for i in [3, 2, 1]:
            idx_map[i][2] = idx_map[i-1][2]
    else:
        # north
        for i in [1, 2, 3]:
            idx_map[i][2] = idx_map[i+1][2]
        
    parallel = (idx_map[2][2]-1) if idx_map[2][2] & 1 else (idx_map[2][2]+1)
    idx_map[0][2] = parallel
    idx_map[2][0] = parallel
    idx_map[2][4] = parallel
    idx_map[4][2] = parallel

y = Y
x = X
while len(cmd) > 0:
    direction = int(cmd.pop(0))-1
    ny = y+dy[direction]
    nx = x+dx[direction]

    if ny < 0 or nx < 0 or ny >= N or nx >= M:
        continue

    y = ny
    x = nx

    move(direction)

    if board[y][x] == 0:
        board[y][x] = dice[idx_map[0][2]]
    else:
        dice[idx_map[0][2]] = board[y][x]
        board[y][x] = 0

    print(dice[idx_map[2][2]])