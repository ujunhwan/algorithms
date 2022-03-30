# https://www.acmicpc.net/problem/7569
# 7569번 토마토

import sys
from collections import deque

input = sys.stdin.readline

def solution():
    # M -> col N -> row H -> height
    M, N, H = map(int, input().split())

    dy = [0, -1, 0, 1, 0, 0]
    dx = [1, 0, -1, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    q = deque()
    
    # floor, row, col
    box = [[] for col in range(H)]
    for h in range(H):
        for n in range(N):
            row = (list(map(int, input().split())))
            box[h].append(row)
            for i in range(M):
                if row[i] == 1:
                    q.append([h, n, i])

    def is_valid(z, y, x):
        return (0 <= z < H and 0 <= y < N and 0 <= x < M) and (box[z][y][x] == 0)

    def bfs():
        ret = -1
        while q:
            z, y, x = q.popleft()
            for k in range(6):
                nz, ny, nx = z + dz[k], y + dy[k], x + dx[k]
                if not is_valid(nz, ny, nx): continue
                box[nz][ny][nx] = box[z][y][x] + 1
                q.append([nz, ny, nx])
                ret = max(ret, box[nz][ny][nx])
                
        return ret 

    if not q:
        print(-1)
        return

    ans = bfs()
    if ans == -1:
        print(0)
    else:
        for b in box:
            for a in b:
                if 0 in a:
                    print(-1)
                    return
        print(ans-1)

solution()

"""

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0


"""