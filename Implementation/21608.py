N = int(input())

N2 = N*N

student = [[] for col in range(N2+1)]
board = [[0 for col in range(N)] for row in range(N)]
seq = []

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

def plus(y, x, score):
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if is_valid(ny, nx):
            score[ny][nx] += 1

def empty_count(y, x):
    cnt = 0
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if is_valid(ny, nx) and board[ny][nx] == 0:
            cnt += 1
    
    return cnt

def calc(idx, y, x):
    cnt = 0
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if is_valid(ny, nx) and board[ny][nx] in student[idx]:
            cnt += 1
    return cnt

def check(idx):
    score = [[0 for col in range(N)] for row in range(N)]
    y, x = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and board[i][j] in student[idx]:
                y, x = i, j
                plus(y, x, score)
    
    val = 0
    like = []
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and val <= score[i][j]:
                if val == score[i][j]:
                    like.append([i, j])
                else:
                    val = score[i][j]
                    like.clear()
                    like.append([i, j])

    y, x = 0, 0
    cnt = -1
    if len(like) > 1:
        # empty max
        for i, j in like:
            cand = empty_count(i, j)
            if cand > cnt:
                cnt = cand
                y, x = i, j
    
    else:
        y, x = like.pop()
    
    board[y][x] = idx


for i in range(N2):
    a = list(map(int, input().split()))
    val = a.pop(0)
    seq.append(val)
    student[val] = a
    check(val)

conv = [0, 1, 10, 100 ,1000]
ans = 0
for i in range(N):
    for j in range(N):
        ans += conv[calc(board[i][j], i, j)]

print(ans)
