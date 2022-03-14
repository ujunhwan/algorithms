# https://www.acmicpc.net/problem/1189
# 1189번 컴백홈

import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
visited = [[0 for col in range(C)] for row in range(R)]

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

ans = 0
def dfs(y, x, cnt):
    global ans

    if cnt > K:
        return

    if y == 0 and x == C-1:
        if cnt == K:
            ans += 1
        return
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < R and 0 <= nx < C and visited[ny][nx] == 0 and arr[ny][nx] == '.':
            visited[ny][nx] = 1
            dfs(ny, nx, cnt+1)
            visited[ny][nx] = 0

visited[R-1][0] = 1
dfs(R-1, 0, 1)

print(ans)