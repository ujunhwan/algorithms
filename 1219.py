# https://www.acmicpc.net/problem/1219
# 1219번 오민식의 고민

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    N, src, goal, M = map(int, input().split())

    path = []
    for i in range(M):
        path.append(list(map(int, input().split())))
    
    money = list(map(int, input().split()))
    adj = [[] for _ in range(N)]

    earn = [-float('inf') for _ in range(N)]

    for a, b, c in path:
        adj[a].append([b, money[b]-c])
    
    is_cycle = False
    earn[src] = money[src]
    cycle = []
    for i in range(N):
        for j in range(N):
            for next, cost in adj[j]:
                if earn[j] != -float('inf') and earn[next] < cost + earn[j]:
                    if i == N-1:
                        cycle.append(next)
                        is_cycle = True
                    earn[next] = cost + earn[j]

    def bfs():
        visited = [False for _ in range(51)]
        q = deque()
        for c in cycle:
            q.append(c)
            visited[c] = True
        while q:
            here = q.popleft()
            for next, cost in adj[here]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
        
        return visited[goal]

    if earn[goal] == -float('inf'):
        print("gg")
    elif is_cycle and bfs():
        print("Gee")
    else:
        print(earn[goal])

solution()