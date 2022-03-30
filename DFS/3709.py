# https://www.acmicpc.net/problem/3709
# 3709번 레이저빔은 어디로 

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

tc = int(input())

def solution():
    N, R = map(int, input().split())

    board = [[0 for col in range(N+2)] for row in range(N+2)]
    adj = [[-1 for col in range(4)] for _ in range(51)]
    mirror = []
    mapping = [[-1, -1] for _ in range(51)]
    visited = [[False for _ in range(4)] for _ in range(51)]

    cnt = 1
    for i in range(R):
        x, y = map(int, input().split())
        mirror.append([x, y])
        board[y][x] = cnt
        mapping[cnt] = [x, y]
        cnt += 1
    lx, ly = map(int, input().split())

    for x, y in mirror:
        num = board[y][x]

        # 나보다 아래에서 오는 녀석
        for i in range(y-1, 0, -1):
            if board[i][x] != 0:
                adj[num][3] = board[i][x]
                break

        # 나보다 위에 있는 녀석 
        for i in range(y+1, N+1):
            if board[i][x] != 0:
                adj[num][1] = board[i][x]
                break

        # 나보다 오른쪽에 있는 놈 
        for i in range(x+1, N+1):
            if board[y][i] != 0:
                adj[num][0] = board[y][i]
                break

        # 나보다 왼쪽에 있는 놈 
        for i in range(x-1, 0, -1):
            if board[y][i] != 0:
                adj[num][2] = board[y][i]
                break
    
    dir = -1
    if ly == 0:
        dir = 1
        for i in range(N+1):
            if board[i][lx] != 0:
                ly = i
                break
    elif ly == N+1:
        dir = 3
        for i in range(N, 0, -1):
            if board[i][lx] != 0:
                ly = i
                break
    elif lx == 0:
        dir = 0
        for i in range(N+1):
            if board[ly][i] != 0:
                lx = i
                break
    else:
        dir = 2
        for i in range(N, 0, -1):
            if board[ly][i] != 0:
                lx = i
                break
    
    def calc(x, y, dir):
        if dir == 0:
            return f"{N+1} {y}"
        elif dir == 1:
            return f"{x} {N+1}"
        elif dir == 2:
            return f"{0} {y}"
        else:
            return f"{x} {0}"

    def dfs(idx, dir):
        visited[idx][dir] = True
        next_dir = (dir-1)%4
        next = adj[idx][next_dir]
        # print(f"현재 인덱스 : {mapping[idx]} {dir}")
        # print(f"다음 노드와 방향 : {next} {next_dir}")

        if next == -1:
            x, y = mapping[idx]
            print(calc(x, y, (dir-1)%4))
            return
        elif visited[next][next_dir]:
            print("0 0")
            return
        dfs(next, next_dir)
    
    if board[ly][lx] <= 0:
        print(calc(lx, ly, dir))
    else:
        dfs(board[ly][lx], dir)

for i in range(tc):
    solution()

"""
1
2 3
1 1
1 2
2 2
3 1

ans : 2 0

1
2 1
1 1
0 1

ans : 1 0

1
3 6
1 1
1 3
2 2
2 3
3 1
3 2
2 0

ans : 0 2

1
2 1
1 1
0 2

ans : 3 2
"""