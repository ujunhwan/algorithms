'''
i번째 원판의 j 위치 = (i, j)
'''

N, M, T = map(int, input().split())

circle = [[0 for col in range(M)] for row in range(N)]
for i in range(N):
    circle[i] = list(map(int, input().split()))

cmd = []
for i in range(T):
    cmd.append(list(map(int, input().split())))


'''
번호 배수인거 따질때 +1 해야함!
번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. 
di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
'''

w = [0 for col in range(N)]

def rotate(num, dir, k):
    # print(f"rotate : {num} {dir} {k}")
    if dir == 0:
        w[num] = (w[num]-k+M)%M
    else:
        w[num] = (w[num]+k+M)%M

def remove():
    lazy = [[0 for col in range(M)] for row in range(N)]
    for i in range(N):
        for j in range(M):
            lazy[i][j] = circle[i][j]

    is_possible = False
    for i in range(N):
        for j in range(M):
            # search adjacent number
            idx = (j + w[i]) % M
            val = circle[i][idx]

            if val == 0:
                continue

            left_idx = ((j+1) + w[i]) % M
            right_idx = ((j-1) + w[i]) % M

            if i-1 >= 0:
                up_idx = (j + w[i - 1]) % M
                if val == circle[i-1][up_idx]:
                    lazy[i-1][up_idx] = 0
                    is_possible = True

            if i+1 < N:
                down_idx = (j + w[i + 1]) % M
                if val == circle[i+1][down_idx]:
                    lazy[i+1][down_idx] = 0
                    is_possible = True

            if val == circle[i][left_idx]:
                lazy[i][left_idx] = 0
                is_possible = True

            if val == circle[i][right_idx]:
                lazy[i][right_idx] = 0
                is_possible = True

    # 한 원판에서 인접한게 있는지?

    if not is_possible:
        circle_sum = 0
        cnt = 0
        for i in range(N):
            circle_sum += sum(circle[i])
            for j in range(M):
                if circle[i][j] == 0:
                    continue
                cnt += 1

        # cnt == 0일 때?
        if cnt > 0:
            mean = circle_sum / cnt

            for i in range(N):
                for j in range(M):
                    if circle[i][j] == 0:
                        continue
                    if circle[i][j] > mean:
                        lazy[i][j] -= 1
                    elif circle[i][j] < mean:
                        lazy[i][j] += 1

    for i in range(N):
        for j in range(M):
            circle[i][j] = lazy[i][j]

# for j in range(M):
#     idx = (j+w[0])%M
#     print(circle[0][idx])
#
# rotate(0, 0, 2)
for x, d, k in cmd:
    '''
    x의 배수인 원판을 d 방향으로 k칸 회전
    '''
    # rotate
    for num in range(x, N+1, x):
        rotate(num-1, d, k)

    # remove
    remove()
    # for i in range(N):
    #     for j in range(M):
    #         idx = (j + w[i]) % M
    #         print(circle[i][idx], end=' ')
    #     print('')




ans = 0
for i in range(N):
    ans += sum(circle[i])

print(ans)