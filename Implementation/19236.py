# 0 up, 1 up_left, 2 left, 3 down_left, 4 down, 5 down_right, 6 right, 7 up_right
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

N = 4

# board[i][j] -> (i, j) fish's number
board = [[0 for col in range(N)] for row in range(N)]

# fish[i] = ith fish's direction
fish_pos = [0 for _ in range(16+1)]
fish_dir = [0 for _ in range(16+1)]

pos = 0
for _ in range(N):
    info = list(map(int, input().split()))
    for i in range(0, 8, 2):
        a, b = info[i], info[i+1]
        board[pos//N][pos%N] = a
        fish_pos[a] = pos
        fish_dir[a] = b-1
        pos += 1

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

def swap(a, b):
    # position
    apos = fish_pos[a]
    bpos = fish_pos[b]

    # map
    ay, ax = apos // N, apos % N
    by, bx = bpos // N, bpos % N

    tmp = board[by][bx]
    board[by][bx] = board[ay][ax]
    board[ay][ax] = tmp

    fish_pos[a] = bpos
    fish_pos[b] = apos

def shark_move(cnt):
    dir = fish_dir[0]
    pos = fish_pos[0]
    y, x = pos // N, pos % N

    is_possible = False
    

    ret = 0

    temp_fish_dir = [0 for col in range(N*N+1)]
    temp_fish_pos = [0 for col in range(N*N+1)]

    for i in range(0, N*N+1):
        temp_fish_dir[i] = fish_dir[i]
        temp_fish_pos[i] = fish_pos[i]

    tmp = [[0 for col in range(N)] for row in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = board[i][j]

    fish_move()

    for d in [1, 2, 3, 4]:
        ny, nx = y + dy[dir]*d, x + dx[dir]*d
        if is_valid(ny, nx) and board[ny][nx] > 0:
            # eat fish
            is_possible = True
            num = board[ny][nx]
            tmp_dir = fish_dir[num]
            tmp_pos = fish_pos[num]

            # get fish's direction, position
            fish_dir[0] = fish_dir[num]
            fish_pos[0] = fish_pos[num]

            # die
            fish_dir[num] = -1
            fish_pos[num] = -1
            board[y][x] = -1

            # map
            board[ny][nx] = 0
                        
            ret = max(ret, shark_move(cnt + num))

            # rollback
            board[y][x] = 0
            board[ny][nx] = num

            fish_dir[0] = dir
            fish_pos[0] = pos

            fish_dir[num] = tmp_dir
            fish_pos[num] = tmp_pos

    fish_rollback(tmp, temp_fish_dir, temp_fish_pos)

    if not is_possible:
        return cnt
    return ret

def fish_move():
    for num in range(1, N*N+1):
        pos = fish_pos[num]
        dir = fish_dir[num]
        if pos == -1 or dir == -1:
            continue
        y, x = pos // N, pos % N
        for k in range(8):
            ndir = (dir + k) % 8
            ny, nx = y + dy[ndir], x + dx[ndir]
            if is_valid(ny, nx) and board[ny][nx] != 0:
                fish_dir[num] = ndir
                if board[ny][nx] == -1:
                    board[ny][nx] = num
                    board[y][x] = -1
                    fish_pos[num] = ny*N+nx
                    break
                else:
                    swap(board[y][x], board[ny][nx])
                    break

def fish_rollback(tmp, temp_fish_dir, temp_fish_pos):
    for i in range(N):
        for j in range(N):
            board[i][j] = tmp[i][j]
    
    for i in range(N*N+1):
        fish_dir[i] = temp_fish_dir[i]
        fish_pos[i] = temp_fish_pos[i]

# shark init
fish_pos[0] = fish_pos[board[0][0]]
fish_dir[0] = fish_dir[board[0][0]]
fish_pos[board[0][0]] = -1
fish_dir[board[0][0]] = -1
num = board[0][0]
board[0][0] = 0

ans = shark_move(num)

print(ans)