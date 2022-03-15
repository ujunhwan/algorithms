# https://www.acmicpc.net/problem/3190
# 3190번 뱀

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())

apple = [[0 for col in range(N)] for row in range(N)]

K = int(input())
for i in range(K):
    y, x = map(int, input().split())
    apple[y-1][x-1] = 1

L = int(input())

move = []

# L left turn 0 D right turn 1
for i in range(L):
    num, char = input().split()
    dir = 0 if char == 'L' else 1
    move.append([int(num), dir])

# head = [y, x, dir]
# dir 0 right, 1 up, 2 left, 3 down
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

tail_move = [] # [시간, 방향]
snake = []
def dfs(d, time, size):
    hy, hx = snake[0]
    hd = d

    # next head dir 
    if len(move) > 0 and move[0][0] == time:
        dir = move[0][1]
        hd = (hd+1)%4 if dir == 0 else (hd-1)%4
        move.pop(0)
    
    # next head point
    ny = hy+dy[hd]
    nx = hx+dx[hd]
    nd = hd

    if ny < 0 or nx < 0 or ny >= N or nx >= N or ([ny, nx] in snake):
        print(time+1)
        exit()
    
    # 사과 있으면 그대로
    if apple[ny][nx] == 1:
        apple[ny][nx] = 0
        snake.insert(0, [ny, nx])
        dfs(nd, time+1, size+1)

    # 사과 없으면 꼬리 한칸 빼기 
    else:
        snake.insert(0, [ny, nx])
        snake.pop(-1)
        dfs(nd, time+1, size)

snake.append([0, 0])
dfs(0, 0, 1)
