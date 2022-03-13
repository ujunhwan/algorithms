# https://www.acmicpc.net/problem/1987
# 1987번 알파벳

R, C = map(int, input().split())

board = [(list(input().rstrip())) for _ in range(R)]

visited = [False] * 27

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

ans = 0

def charIdx(y, x):
    return ord(board[y][x]) - 65

def dfs(y, x, cnt):
    global ans, visited
    
    ans = max(ans, cnt)

    for k in range(4):
        ny, nx = y+dy[k], x+dx[k]

        if 0 <= ny < R and 0 <= nx < C:
            nIdx = charIdx(ny, nx)
            if not visited[nIdx]:
                visited[nIdx] = True
                dfs(ny, nx, cnt+1)
                visited[nIdx] = False

visited[charIdx(0, 0)] = True
dfs(0, 0, 1)
print(ans)