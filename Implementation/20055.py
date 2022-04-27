'''
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
'''


N, K = map(int, input().split())
A = list(map(int, input().split()))

global apos, bpos

apos = 0
bpos = N-1
idx = 0

robot_seq = []
robots = [0 for _ in range(2*N)]

def rotate():
    global apos, bpos
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.

    apos = (apos - 1) % (2*N)
    bpos = (bpos - 1) % (2*N)

    for robot_pos in robot_seq:
        if robot_pos == bpos:
            robots[robot_pos] -= 1
            robot_seq.remove(robot_pos)

def move():
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    #     1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.

    global apos, bpos

    # check
    for robot_pos in robot_seq:
        if robot_pos == bpos:
            robots[robot_pos] -= 1
            robot_seq.remove(robot_pos)

    lazy = []
    # move
    for i in range(len(robot_seq)):
        # move to (i+1) block
        robot_pos = robot_seq[i]
        next_pos = (robot_pos+1)%(2*N)

        # 로봇이 다른 블록으로 이동
        if robots[next_pos] == 0 and A[next_pos] > 0:
            robots[robot_pos] -= 1
            robots[next_pos] += 1
            robot_seq[i] = next_pos
            A[next_pos] -= 1

            # 이동하는 곳이 출구라면 
            if next_pos == bpos:
                lazy.append(bpos)

    for l in lazy:
        robot_seq.remove(l)
        robots[bpos] -= 1

def add():
    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    global apos, bpos
    if A[apos] > 0:
        robots[apos] += 1
        robot_seq.append(apos)
        A[apos] -= 1

def is_done():
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    cnt = 0
    for a in A:
        if a == 0:
            cnt += 1
    if cnt >= K:
        return True
    return False

ans = 0
while not is_done():
    rotate()
    move()
    add()
    ans += 1

print(ans)

'''
3 2
0 0 0 0 0 0
3 2
1 2 1 2 1 2
ans : [0 1 0 2 1 2]
'''