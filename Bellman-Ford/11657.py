# https://www.acmicpc.net/problem/11657
# 11657번 타임머신

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    global is_cycle
    N, M = map(int, input().split())

    adj = [[] for col in range(N+1)]
    dist = [float('inf') for _ in range(N+1)]
    is_cycle = False

    for i in range(M):
        a, b, c = map(int, input().split())
        adj[a].append([b, c])
    
    def bellman_ford():
        global is_cycle
        dist[1] = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                for next, cost in adj[j]:
                    if dist[j] != float('inf') and dist[next] > dist[j] + cost:
                        dist[next] = dist[j] + cost
                        if i == N:
                            is_cycle = True
    
    bellman_ford()

    if is_cycle:
        print(-1)
        return
    
    for i in range(2, N+1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])

solution()