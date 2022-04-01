# https://www.acmicpc.net/problem/1162
# 1162번 도로 포장

import sys, heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    N, M, K = map(int, input().split())
    adj = [[] for _ in range(N+1)]

    for i in range(M):
        p, q, d = map(int, input().split())
        adj[p].append([d, q])
        adj[q].append([d, p])

    dist = [[float('inf') for _ in range(21)] for _ in range(N+1)]

    for i in range(21):
        dist[0][i] = 0
        dist[1][i] = 0

    def dijkstra():
        pq = []
        heapq.heappush(pq, [0, 1, K])
        while pq:
            cost, node, left = heapq.heappop(pq)
            if cost > dist[node][left]: continue
            for c, next_node in adj[node]:
                next_cost = cost + c
                if dist[next_node][left] > next_cost:
                    dist[next_node][left] = next_cost
                    heapq.heappush(pq, [next_cost, next_node, left])
                
                next_cost = cost
                if left > 0 and dist[next_node][left-1] > next_cost:
                    dist[next_node][left-1] = next_cost
                    heapq.heappush(pq, [next_cost, next_node, left-1])

    dijkstra()

    ans = float('inf')
    for cand in dist[N]:
        ans = min(ans, cand)

    print(ans)

solution()

"""
4 4 1
1 2 10
2 4 10
3 4 3
1 3 100

ans : 3



"""