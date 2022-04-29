global ans
R, C, K = map(int, input().split())
room = [0 for row in range(R*C)]
board = [0 for col in range(R*C)]
wall = [[False for col in range(2)] for row in range(R*C)]
test_pos = []
warm_pos = []

for i in range(R):
    r = list(map(int, input().split()))
    for j in range(C):
        room[i*C+j] = r[j]
        if r[j] == 0: continue
        if r[j] == 5:
            test_pos.append(i*C+j)
        else:
            warm_pos.append(i*C+j)

W = int(input())

for i in range(W):
    # 0 -> 세로를 막는벽 1 -> 가로를 막는벽
    y, x, t = map(int, input().split())
    wall[(y-1)*C+(x-1)][t] = True

# right left up down
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

vy = [[-1, 0, 1], [-1, 0, 1], [-1, -1, -1], [1, 1, 1]]
vx = [[1, 1, 1], [-1, -1, -1], [-1, 0, 1], [-1, 0, 1]]

'''
1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
2. 온도가 조절됨
3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
4. 초콜릿을 하나 먹는다.
5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
'''

def debug_board():
    for i in range(R):
        print(board[i*C:i*C+C])
    print('#####')

def debug_lazy(lazy):
    print("LAZYYYYY")
    for i in range(R):
        print(lazy[i*C:i*C+C])
    print('#####')


def is_valid(y, x):
    return 0 <= y < R and 0 <= x < C

def is_valid_pos(pos):
    return is_valid(pos//C, pos%C)

def is_wall(y, x, dir):
    # y, x 에서 dir로 가는 길에 벽이 막고있나요?

    right = y*C+(x+1)
    left = y*C+(x-1)
    up = (y-1)*C+x
    down = (y+1)*C+x
    pos = y*C+x

    if dir == 0:
        if wall[pos][1]:
            return True

    elif dir == 1:
        if wall[right][1]:
            return True
    
    elif dir == 2:
        if wall[pos][0]:
            return True
    
    elif dir == 3:
        if wall[down][0]:
            return True

    return False

def is_done():
    global ans
    ans += 1
    if ans > 100:
        ans = 101
        return True
    for t in test_pos:
        if board[t] < K:
            return False
    return True

def right_move(y, x, state):
    right = y*C+(x+1)
    left = y*C+(x-1)
    up = (y-1)*C+x
    down = (y+1)*C+x
    pos = y*C+x
    up_right = (y-1)*C+(x+1)
    up_left = (y-1)*C+(x-1)
    down_right = (y+1)*C+(x+1)
    down_left = (y+1)*C+(x-1)

    if state == 0:
        if is_valid_pos(up):
            if not wall[pos][0] and not wall[up][1]:
                return True
    elif state == 1:
        if not wall[pos][1]:
            return True
    else:
        if is_valid_pos(down):
            if not wall[down][0] and not wall[down][1]:
                return True
    return False

def left_move(y, x, state):
    right = y*C+(x+1)
    left = y*C+(x-1)
    up = (y-1)*C+x
    down = (y+1)*C+x
    pos = y*C+x
    up_right = (y-1)*C+(x+1)
    up_left = (y-1)*C+(x-1)
    down_right = (y+1)*C+(x+1)
    down_left = (y+1)*C+(x-1)

    if state == 0:
        if is_valid_pos(up_left):
            if not wall[pos][0] and not wall[up_left][1]:
                return True
    elif state == 1:
        if is_valid_pos(left):
            if not wall[left][1]:
                return True
    else:
        if is_valid_pos(down) and is_valid_pos(down_left):
            if not wall[down][0] and not wall[down_left][1]:
                return True
    return False

def down_move(y, x, state):
    right = y*C+(x+1)
    left = y*C+(x-1)
    up = (y-1)*C+x
    down = (y+1)*C+x
    pos = y*C+x
    up_right = (y-1)*C+(x+1)
    up_left = (y-1)*C+(x-1)
    down_right = (y+1)*C+(x+1)
    down_left = (y+1)*C+(x-1)

    if state == 0:
        if is_valid_pos(left) and is_valid_pos(down_left):
            if not wall[left][1] and not wall[down_left][0]:
                return True
    elif state == 1:
        if is_valid_pos(down):
            if not wall[down][0]:
                return True
    else:
        if is_valid_pos(down_right):
            if not wall[pos][1] and not wall[down_right][0]:
                return True
    return False

def up_move(y, x, state):
    right = y*C+(x+1)
    left = y*C+(x-1)
    up = (y-1)*C+x
    down = (y+1)*C+x
    pos = y*C+x
    up_right = (y-1)*C+(x+1)
    up_left = (y-1)*C+(x-1)
    down_right = (y+1)*C+(x+1)
    down_left = (y+1)*C+(x-1)

    if state == 0:
        if is_valid_pos(left):
            if not wall[left][1] and not wall[left][0]:
                return True
    elif state == 1:
        if not wall[pos][0]:
            return True
    else:
        if is_valid_pos(right):
            if not wall[pos][1] and not wall[right][0]:
                return True
    return False

def inc_temp(y, x, dir):
    '''
    어떤 칸 (x, y)에 온풍기 바람이 도착해 온도가 k (> 1)만큼 상승했다면, 
    (x-1, y+1), (x, y+1), (x+1, y+1)의 온도도 k-1만큼 상승하게 된다.
    이때 그 칸이 존재하지 않는다면, 바람은 이동하지 않는다. 
    온풍기에서 바람이 한 번 나왔을 때, 어떤 칸에 같은 온풍기에서 나온 바람이 여러 번 도착한다고 해도 온도는 여러번 상승하지 않는다.
    '''

    '''
    일부 칸과 칸 사이에는 벽이 있어 온풍기 바람이 지나갈 수 없다. 
    바람이 오른쪽으로 불었을 때 어떤 칸 (x, y)에서 (x-1, y+1)로 바람이 이동할 수 있으려면, 
    (x, y)와 (x-1, y) 사이에 벽이 없어야 하고, (x-1, y)와 (x-1, y+1) 사이에도 벽이 없어야 한다. 
    (x, y)에서 (x, y+1)로 바람이 이동할 수 있으려면 (x, y)와 (x, y+1) 사이에 벽이 없어야 한다. 
    마지막으로 (x, y)에서 (x+1, y+1)로 바람이 이동할 수 있으려면, 
    (x, y)와 (x+1, y), (x+1, y)와 (x+1, y+1) 사이에 벽이 없어야 한다.
    '''

    lazy = [0 for _ in range(R*C)]
    lazy[y*C+x] += 5
    q = []
    q.append(y*C+x)
    while q:
        pos = q.pop(0)
        cy, cx = pos // C, pos % C
        k = lazy[pos]

        for i in range(0, 3):
            ny, nx = cy + vy[dir][i], cx + vx[dir][i]
            npos = ny*C+nx
            if is_valid(ny, nx) and lazy[npos] == 0 and k > 0:
                # right left up down
                if dir == 0 and right_move(cy, cx, i):
                    q.append(npos)
                    lazy[npos] += (k-1)
                elif dir == 1 and left_move(cy, cx, i):
                    q.append(npos)
                    lazy[npos] += (k-1)
                elif dir == 2 and up_move(cy, cx, i):
                    q.append(npos)
                    lazy[npos] += (k-1)
                elif dir == 3 and down_move(cy, cx, i):
                    q.append(npos)
                    lazy[npos] += (k-1)

    for i in range(R*C):
        board[i] += lazy[i]

def control():
    '''
    모든 인접한 칸에 대해서, 온도가 높은 칸에서 낮은 칸으로 ⌊(두 칸의 온도의 차이)/4⌋만큼 온도가 조절된다.
    온도가 높은 칸은 이 값만큼 온도가 감소하고, 낮은 칸은 온도가 상승한다.
    인접한 두 칸 사이에 벽이 있는 경우에는 온도가 조절되지 않는다.
    이 과정은 모든 칸에 대해서 동시에 발생한다.
    '''

    lazy = [0 for _ in range(R*C)]

    for pos in range(R*C):
        y, x = pos // C, pos % C
        for dir in [0, 3]:
            ny, nx = y + dy[dir], x + dx[dir]
            npos = ny*C+nx
            if is_valid(ny, nx) and not is_wall(y, x, dir):
                diff = 0
                if board[pos] > board[npos]:
                    diff = int((board[pos] - board[npos]) / 4)
                    if board[pos] > 0:
                        lazy[pos] -= diff
                    lazy[npos] += diff
                else:
                    diff = int((board[npos] - board[pos]) / 4)
                    lazy[pos] += diff
                    if board[npos] > 0:
                        lazy[npos] -= diff

    for i in range(R*C):
        board[i] += lazy[i]

def exec_warmer():
    for warm in warm_pos:
        dir = room[warm] - 1
        y, x = warm//C + dy[dir], warm%C + dx[dir]
        inc_temp(y, x, dir)

def decrease():
    for j in range(1, C-1):
        if board[0*C+j] >= 1:
            board[0*C+j] -= 1

        if board[(R-1)*C+j] >= 1:
            board[(R-1)*C+j] -= 1
    
    for i in range(1, R-1):
        if board[i*C+0] >= 1:
            board[i*C+0] -= 1
        
        if board[i*C+(C-1)] >= 1:
            board[i*C+(C-1)] -= 1
    
    if board[0] >= 1:
        board[0] -= 1
    if board[C-1] >= 1:
        board[C-1] -= 1
    if board[(R-1)*C] >= 1:
        board[(R-1)*C] -= 1
    if board[(R-1)*C+(C-1)] >= 1:
        board[(R-1)*C+(C-1)] -= 1

ans = 0
while 1:
    exec_warmer()
    control()
    decrease()
    if is_done():
        break
print(ans)

'''
[그림 2]
9 6 5
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0

[그림 4]
7 8 5
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1
2 4 0

[그림 5]
7 8 5
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
2
1 4 1
2 4 0

[그림 7]
7 8 5
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0
3
3 4 0
3 3 1
3 5 1

[그림 8]
7 8 5
0 0 0 0 0 0 0 0
0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0
3
3 4 0
3 3 1
3 5 1


3 3 10
0 0 0
0 46 0
0 2 0
1
1 1 1

3 3 10
0 0 0
0 0 0
0 0 0
3
2 2 1
1 3 0
3 2 0


'''

