'''
택시는 특이하게도 손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝난다.
'''

'''
현재 위치에서 최단거리가 가장 짧은 승객을 고른다.
그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을,
그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다. 
'''

'''
한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다. 
이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다.
승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
'''
import heapq

N, M, fuel = map(int, input().split())

board = [[0 for col in range(N)] for row in range(N)]
left_guest = [i for i in range(1, M+1)]

for i in range(N):
    board[i] = list(map(int, input().split()))

iy, ix = map(int, input().split())

# guest number 1 ~ M
start = [-1 for _ in range(M+1)]
end = [-1 for _ in range(M+1)]
dist = [float('inf') for _ in range(M+1)]

for i in range(1, M+1):
    sy, sx, ey, ex = map(int, input().split())
    start[i] = (sy-1)*N+(sx-1)
    end[i] = (ey-1)*N+(ex-1)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N and board[y][x] == 0

def dijkstra(src, d):
    d[src] = 0
    q = []
    heapq.heappush(q, [0, src])
    while q:
        cost, pos = heapq.heappop(q)
        y, x = pos // N, pos % N
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            npos = ny*N+nx
            if is_valid(ny, nx) and d[npos] > cost + 1:
                d[npos] = cost + 1
                heapq.heappush(q, [cost+1, npos])

# for i in range(1, M+1):
    # dist[i] = bfs(start[i], end[i])
    # if dist[i] == float('inf'):
    #     print(-1)
    #     exit(0)

# take first guest
taxi = (iy-1)*N+(ix-1)

visited = [False for _ in range(M+1)]

for _ in range(M):
    guest_pos = float('inf')
    guest_num = 0
    min_dist = float('inf')
    dist_list = [float('inf') for _ in range(N*N)]
    dijkstra(taxi, dist_list)
    for i in range(1, M+1):
        if visited[i]:
            continue
        d = dist_list[start[i]]

        # print(f"d = {d} i = {i}")
        if min_dist == d:
            if guest_pos > start[i]:
                guest_num = i
                guest_pos = start[i]
        elif min_dist > d:
            min_dist = d
            guest_num = i
            guest_pos = start[i]
    '''
    for i in range(1, M+1):
        if visited[i]:
            continue
        d = bfs(taxi, start[i])
        if min_dist == d:
            if guest_pos > start[i]:
                guest_num = i
                guest_pos = start[i]
        elif min_dist > d:
            min_dist = d
            guest_num = i
            guest_pos = start[i]
    '''

    if guest_num == 0 or min_dist == float('inf'):
        break

    # pick up
    if fuel - min_dist <= 0:
        break
    fuel -= min_dist

    dist_list = [float('inf') for _ in range(N*N)]
    dijkstra(guest_pos, dist_list)

    # drive
    end_pos = end[guest_num]
    drive_dist = dist_list[end_pos]
    if fuel - dist_list[end_pos] < 0:
        break
    fuel += dist_list[end_pos]

    taxi = end[guest_num]
    visited[guest_num] = True

# print(visited)
for i in range(1, M+1):
    if not visited[i]:
        print(-1)
        exit(0)
print(fuel)
'''
10 1 5000
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
5 5
10 10 5 5
'''