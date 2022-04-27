global ans
ans = 0
N = int(input())

board = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))

# 좌 하 우 상
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

'''
N은 홀수
가운데 모래는 0
토네이도의 현재 값은 0 밀어냄
'''

def is_valid(y, x, val):
    global ans
    if 0 <= y < N and 0 <= x < N:
        return True
    ans += val

def effect(y, x, dir):
    global ans

    # dir odd -> vertical
    # dir even -> horitzontal

    val = board[y][x]
    one = int(val / 100)
    two = int(val * 2 / 100)
    sev = int(val / 100 * 7)
    ten = int(val / 100 * 10)
    five = int(val / 100 * 5)
    left = val - (one+two+sev+ten)*2 - five
    board[y][x] = 0

    by, bx = y-dy[dir], x-dx[dir]
    ay, ax = y+dy[dir], x+dx[dir]

    if dir&1 == 1:
        # vertical
        if is_valid(by, bx+1, one):
            board[by][bx+1] += one
        if is_valid(by, bx-1, one):
            board[by][bx-1] += one

        if is_valid(y, x+2, two):
            board[y][x+2] += two
        if is_valid(y, x-2, two):
            board[y][x-2] += two

        if is_valid(y, x+1, sev):
            board[y][x+1] += sev
        if is_valid(y, x-1, sev):
            board[y][x-1] += sev

        if is_valid(ay, ax+1, ten):
            board[ay][ax+1] += ten
        if is_valid(ay, ax-1, ten):
            board[ay][ax-1] += ten
    else:
        # horizontal
        if is_valid(by+1, bx, one):
            board[by+1][bx] += one
        if is_valid(by-1, bx, one):
            board[by-1][bx] += one

        if is_valid(y+2, x, two):
            board[y+2][x] += two
        if is_valid(y-2, x, two):
            board[y-2][x] += two

        if is_valid(y-1, x, sev):
            board[y-1][x] += sev
        if is_valid(y+1, x, sev):
            board[y+1][x] += sev

        if is_valid(ay+1, ax, ten):
            board[ay+1][ax] += ten
        if is_valid(ay-1, ax, ten):
            board[ay-1][ax] += ten

    if is_valid(ay, ax, left):
        board[ay][ax] += left

    if is_valid(ay+dy[dir], ax+dx[dir], five):
        board[ay+dy[dir]][ax+dx[dir]] += five

k = 0

y, x = N//2, N//2
dir = 0
cnt = 0
is_finished = False
while 1:
    if cnt == 0:
        k += 1
    for i in range(k):
        if y == 0 and x == 0:
            print(ans)
            exit(0)
        ny, nx = y + dy[dir], x + dx[dir]
        effect(ny, nx, dir)
        y, x = ny, nx

    dir = (dir+1)%4
    cnt = (cnt+1)%2