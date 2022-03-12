# https://www.acmicpc.net/problem/1045
# 1045번 도로

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
uf = [-1] * ((N+1) ** 2)

def find(u):
    if uf[u] < 0:
        return u
    uf[u] = find(uf[u])
    return uf[u]

def merge(u, v):
    u, v = find(u), find(v)
    if u == v: return
    uf[u] = v

adj = [[0 for col in range(N)] for row in range(N)]

for i in range(N):
    roads = list(input().rstrip())
    for j in range(N):
        if roads[j] == 'Y':
            adj[i][j] = 1
        else:
            adj[i][j] = 0

edges = []

ans = [0] * N

for i in range(0, N):
    for j in range(0, N):
        if i > j or adj[i][j] == 0: continue
        if find(i) == find(j):
            edges.append([i, j])
        else:
            merge(i, j)
            ans[i] += 1
            ans[j] += 1

for i in range(N):
    for j in range(i+1, N):
        if(find(i) != find(j)):
            print(-1)
            exit()

for i in range(M-N+1):
    if len(edges) == 0:
        print(-1)
        exit()
    u, v = edges.pop(0)
    ans[u] += 1
    ans[v] += 1

for i in ans:
    print(i)