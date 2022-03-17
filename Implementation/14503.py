# https://www.acmicpc.net/problem/14503
# 14503번 로봇 청소기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for row in range(N)]
visited = [[False for col in range(M)] for row in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

y = r
x = c

visited[y][x] = 1
ans = 1
while 1:
    isPossible = False

    # 왼쪽방향 탐색
    for k in range(1, 5):
        ny = y + dy[(d-k)%4]
        nx = x + dx[(d-k)%4]

        if ny < 0 or nx < 0 or ny >= N or nx >= M:
            continue

        # 청소 안한 구역이 있을 때
        if not visited[ny][nx] and board[ny][nx] == 0:
            # 회전해서 한칸 가고
            y = ny
            x = nx
            d = (d-k)%4

            # 청소한다
            ans += 1
            isPossible = True
            visited[y][x] = True
            break
    
    # 네 방향 모두 청소 or 벽
    if not isPossible:
        k = (d-2)%4
        backY = y + dy[k]
        backX = x + dx[k]

        # 뒷쪽이 벽이라면
        if board[backY][backX] == 1:
            break
        else:
            # 벽이 아니라면 한 칸 후진
            y = backY
            x = backX
    
print(ans)