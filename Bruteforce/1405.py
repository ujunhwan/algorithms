# https://www.acmicpc.net/problem/1405
# 1405번 미친 로봇

import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
N = arr.pop(0)

# e w s n
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

total = 4 ** N
visited = [[0 for col in range(30)] for row in range(30)]

prob = 1
ans = 0
def dfs(left, y, x):
    global ans, prob

    if left == 0:
        ans += prob
        return

    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if visited[ny][nx] == 0 and arr[k] > 0:
            visited[ny][nx] = 1
            prob *= (arr[k] / 100)

            dfs(left-1, ny, nx)

            visited[ny][nx] = 0
            prob /= (arr[k] / 100)

visited[15][15] = 1
dfs(N, 15, 15)

print(ans)