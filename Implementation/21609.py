from collections import deque
import heapq

N, M = map(int, input().split())
board = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

def rotate():
    # 반시계 90도로 회전 
    row = [[0 for col in range(N)] for row in range(N)]
    for j in range(N-1, -1, -1):
        for i in range(N):
            row[N-1-j][i] = board[i][j]

    for i in range(N):
        for j in range(N):
            board[i][j] = row[i][j]

def gravity():
    # check each row
    for j in range(N):
        blank = -1
        for i in range(N-1, -1, -1):
            if board[i][j] == -2:
                blank = max(blank, i)
            elif board[i][j] == -1:
                blank = i-1
            else:
                if blank >= 0 and blank >= i:
                    tmp = board[blank][j]
                    board[blank][j] = board[i][j]
                    board[i][j] = tmp
                    if tmp == -2:
                        blank -= 1
                    else:
                        blank = i-1

def bfs(y, x):
    a, b = y, x
    cnt, rb = 0, 0
    visited = [[False for col in range(N)] for row in range(N)]
    q = deque()
    val = board[y][x]
    visited[y][x] = True
    q.append([y, x])
    while q:
        y, x = q.popleft()

        if board[y][x] != 0:
            if a > y:
                a, b = y, x
            elif a == y:
                if b > x:
                    a, b = y, x
        
        cnt += 1
        if board[y][x] == 0:
            rb += 1

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if is_valid(ny, nx) and not visited[ny][nx] and (board[ny][nx] == val or board[ny][nx] == 0):
                visited[ny][nx] = True
                q.append([ny, nx])
    
    return cnt, rb, [a, b]

def remove(y, x):
    cnt = 0
    visited = [[False for col in range(N)] for row in range(N)]
    q = deque()
    val = board[y][x]
    visited[y][x] = True
    q.append([y, x])
    while q:
        cnt += 1
        y, x = q.popleft()
        board[y][x] = -2

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if is_valid(ny, nx) and not visited[ny][nx] and (board[ny][nx] == val or board[ny][nx] == 0):
                visited[ny][nx] = True
                q.append([ny, nx])
    
    return cnt

ans = 0

while 1:
    # find which group is best
    h = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                a, b, [y, x] = bfs(i, j)
                heapq.heappush(h, [-a, -b, -y, -x])
    
    if len(h) < 1:
        break
    cand = heapq.heappop(h)
    if -cand[0] < 2 or cand[0] == cand[1]:
       break 

    score = remove(-cand[2], -cand[3])
    ans += (score * score)
    gravity()
    rotate()
    gravity()

print(ans)