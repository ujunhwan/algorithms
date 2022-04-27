N, M, K = map(int, input().split())

mass_board = [[0 for col in range(8)] for row in range(N*N)]
speed_board = [[0 for col in range(8)] for row in range(N*N)]
cnt_board = [[0 for col in range(8)] for row in range(N*N)]

for i in range(M):
    y, x, m, s, d = map(int, input().split())
    pos = (y-1)*N+(x-1)
    mass_board[pos][d] += m
    speed_board[pos][d] += s
    cnt_board[pos][d] += 1

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def move(pos, dir, speed):
    y, x = pos // N, pos % N
    ny, nx = (y + dy[dir]*speed+N) % N, (x + dx[dir]*speed+N) % N
    npos = ny*N+nx

    lazy_mass[npos][dir] += mass_board[pos][dir]
    lazy_mass[pos][dir] -= mass_board[pos][dir]

    lazy_speed[npos][dir] += speed_board[pos][dir]
    lazy_speed[pos][dir] -= speed_board[pos][dir]

    lazy_cnt[npos][dir] += cnt_board[pos][dir]
    lazy_cnt[pos][dir] -= cnt_board[pos][dir]

def merge(pos):
    mass_sum = sum(mass_board[pos])
    speed_sum = sum(speed_board[pos])
    cnt_sum = sum(cnt_board[pos])

    is_even = False
    is_odd = False

    # 방향
    dir_sum = 0
    for dir in range(8):
        cnt = cnt_board[pos][dir]
        if cnt > 0:
            dir_sum += cnt*dir
            if dir & 1 == 1:
                is_odd = True
            else:
                is_even = True
    
    # 합쳐졌으니 초기화
    for dir in range(8):
        mass_board[pos][dir] = 0
        speed_board[pos][dir] = 0
        cnt_board[pos][dir] = 0

    # divide
    new_mass = int(mass_sum / 5)
    new_speed = int(speed_sum / cnt_sum)
    new_dir = [1, 3, 5, 7] if (is_odd and is_even) else [0, 2, 4, 6]

    if new_mass > 0:
        for dir in new_dir:
            speed_board[pos][dir] += new_speed
            mass_board[pos][dir] += new_mass
            cnt_board[pos][dir] += 1

for _ in range(K):
    lazy_mass = [[0 for col in range(8)] for row in range(N*N)]
    lazy_speed = [[0 for col in range(8)] for row in range(N*N)]
    lazy_cnt = [[0 for col in range(8)] for row in range(N*N)]

    # move
    for pos in range(N*N):
        for dir in range(8):
            if cnt_board[pos][dir] > 0:
                move(pos, dir, speed_board[pos][dir])

    # lazy
    for pos in range(N*N):
        for dir in range(8):
            speed_board[pos][dir] += lazy_speed[pos][dir]
            mass_board[pos][dir] += lazy_mass[pos][dir] 
            cnt_board[pos][dir] += lazy_cnt[pos][dir]

    # merge
    for pos in range(N*N):
        cnt = sum(cnt_board[pos])
        if cnt >= 2:
            merge(pos)

ans = 0
for pos in range(N*N):
    ans += sum(mass_board[pos])

print(ans)