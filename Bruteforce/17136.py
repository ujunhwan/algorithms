# https://www.acmicpc.net/problem/17136
# 17136번 색종이 붙이기

import sys
input = sys.stdin.readline

board = [(list(map(int, input().split()))) for _ in range(10)]
visited = [[0 for col in range(10)] for row in range(10)]
left = [0, 5, 5, 5, 5, 5]
ans = 987654321
cand = 0

def draw(row, col):
    global ans, cand

    if row == 10:
        ans = min(cand, ans)
        return

    if col == 10:
        draw(row+1, 0)
        return

    if board[row][col] == 0:
        draw(row, col+1)
        return

    for size in range(1, 6):
        if row+size > 10 or col+size > 10 or left[size] <= 0:
            continue 

        isPossible = True

        for i in range(row, row+size):
            for j in range(col, col+size):
                if board[i][j] == 0:
                    isPossible = False
                    if not isPossible:
                        break
        
        if isPossible:
            for i in range(row, row+size):
                for j in range(col, col+size):
                    board[i][j] = 0
            left[size] -= 1
            cand += 1

            draw(row, col+size)

            for i in range(row, row+size):
                for j in range(col, col+size):
                    board[i][j] = 1
            left[size] += 1
            cand -= 1

draw(0, 0)

if ans == 987654321:
    print(-1)
else:
    print(ans)

"""
1 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 1 1 1 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0 1 1

1 1 0 1 1 0 1 1 0 0
1 1 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0
1 1 0 1 1 0 1 1 0 0
1 1 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

ans : 9

1 1 0 1 1 0 1 1 0 0
1 1 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0
1 1 0 1 1 0 1 1 0 0
1 1 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1

ans : 11

1 0 0 1 1 0 1 1 0 0
1 1 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0
1 0 0 1 1 0 1 1 0 0
1 1 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1

ans : -1

1 1 0 1 1 0 1 1 0 0
1 1 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0
1 1 0 1 1 0 1 1 0 0
1 1 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

ans : -1

1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1 0 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

ans : -1

0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 1 0
0 0 1 1 1 1 1 1 1 0
0 0 1 1 1 1 1 1 1 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

ans : 7

"""