import heapq

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


for tc in range(1, 1000000):
    N = int(input())
    if N == 0:
        break

    def is_valid(y, x):
        return 0 <= y < N and 0 <= x < N

    board = [[0 for col in range(N)] for row in range(N)]
    for i in range(N):
        board[i] = list(map(int, input().split()))

    q = list()
    dist = [[987654321 for col in range(N)] for row in range(N)]
    dist[0][0] = board[0][0]
    heapq.heappush(q, [board[0][0], 0])

    while q:
        cost, pos = heapq.heappop(q)
        y, x = pos//N, pos%N

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if is_valid(ny, nx):
                if dist[ny][nx] > board[ny][nx] + cost:
                    dist[ny][nx] = board[ny][nx] + cost
                    heapq.heappush(q, [dist[ny][nx], ny*N+nx])
    
    print(f"Problem {tc}: {dist[N-1][N-1]}")

    