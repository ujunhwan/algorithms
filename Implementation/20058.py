n, Q = map(int, input().split())

N = (2 ** n)
board = [[] for col in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))

magic = list(map(int, input().split()))

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

def rotate(a, L):
    row = [[0 for col in range(L)] for row in range(L)]
    for j in range(L):
        for i in range(L):
            row[j][i] = a[L-i-1][j]
    
    for i in range(L):
        for j in range(L):
            a[i][j] = row[i][j]

def divide(l):
    if l == 0:
        return
    L = (2**l)
    for i in range(0, N, L):
        for j in range(0, N, L):
            partition = []
            for k in range(i, i+L):
                partition.append(board[k][j:j+L])
            rotate(partition, L)
            adjust(partition, i, j, L)

def adjust(partition, y, x, L):
    for i in range(y, y+L):
        for j in range(x, x+L):
            board[i][j] = partition[i-y][j-x]

def decrease():
    lazy = [[0 for col in range(N)] for row in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] <= 0:
                continue
            adj = 0
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
                if is_valid(ny, nx) and board[ny][nx] > 0:
                    adj += 1

            if adj < 3:
                lazy[i][j] -= 1
    
    for i in range(N):
        for j in range(N):
            board[i][j] += lazy[i][j]

def bfs(init, visited):
    cnt = 0
    q = []
    q.append(init)
    while q:
        cnt += 1
        pos = q.pop(0)
        y, x = pos // N, pos % N
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if is_valid(ny, nx) and not visited[ny][nx] and board[ny][nx] > 0:
                q.append(ny*N+nx)
                visited[ny][nx] = True
    return cnt

def check_sum():
    cnt = 0
    for i in range(N):
        cnt += sum(board[i])
    print(cnt)

def check_mass():
    mass = 0
    visited = [[False for col in range(N)] for row in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                mass = max(mass, bfs(i*N+j, visited))
    print(mass)

for mm in magic:
    divide(mm)
    decrease()

check_sum()
check_mass()

"""
3 1
1 2 3 4 5 6 7 8 
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
49 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64
1

3 1
1 2 3 4 5 6 7 8 
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
49 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64
2
"""