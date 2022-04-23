from collections import deque

def solution():
    N, M, K = map(int, input().split())
    board = list(list(map(int, input().split())) for row in range(N))

    dice = [0] * 6
    dice[0] = 2
    dice[1] = 4
    dice[2] = 1
    dice[3] = 3
    dice[4] = 5
    dice[5] = 6

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    score = [[0 for col in range(M)] for row in range(N)]

    def is_valid(y, x):
        return 0 <= y < N and 0 <= x < M
    
    def next_dir(dir, y, x):
        A = dice[5]
        B = board[y][x]

        # print(f"dir = {dir} A = {A}, board[{y}][{x}] = B = {B}")

        if A > B:
            return (dir+1)%4
        elif A < B:
            return (dir+3)%4
        elif A == B:
            return dir

    def rolling(dir):
        # east
        if dir == 0:
            tmp = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[3]
            dice[3] = dice[2]
            dice[2] = tmp

        # south
        elif dir == 1:
            tmp = dice[0]
            dice[0] = dice[5]
            dice[5] = dice[4]
            dice[4] = dice[2]
            dice[2] = tmp

        # west
        elif dir == 2:
            tmp = dice[1]
            dice[1] = dice[2]
            dice[2] = dice[3]
            dice[3] = dice[5]
            dice[5] = tmp
            
        # north
        elif dir == 3:
            tmp = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[4]
            dice[4] = dice[5]
            dice[5] = tmp

    def bfs(y, x):
        if score[y][x] != 0:
            return score[y][x]
        cnt = 1
        visited = [[False for col in range(M)] for row in range(N)]
        cand = list()
        cand.append([y, x])
        q = deque()
        visited[y][x] = True
        q.append([y, x])
        val = board[y][x]

        while q:
            cur = q.popleft()
            y, x = cur
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if is_valid(ny, nx) and not visited[ny][nx] and board[ny][nx] == val:
                    visited[ny][nx] = True
                    q.append([ny, nx])
                    cand.append([ny, nx])
                    cnt += 1

        for y, x in cand:
            score[y][x] = val*cnt

        return val*cnt
    
    def move(d, y, x):
        rolling(d)
        return y + dy[d], x + dx[d]
    
    def calc_next(dir, y, x):
        dir = next_dir(dir, y, x)

        ny, nx = y + dy[dir], x + dx[dir]

        if not is_valid(ny, nx):
            dir = (dir+2)%4
            return dir, y, x
        
        return dir, y, x 

    d = 0
    ans = 0
    y, x = 0, 0
    for i in range(K):
        ny, nx = move(d, y, x)
        ans += bfs(ny, nx)
        d, y, x = calc_next(d, ny, nx)

    print(ans)

solution()

'''
4 5 9 
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5

ans : 55

4 5 8
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5


'''