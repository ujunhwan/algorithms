# https://www.acmicpc.net/problem/1922
# 1922번 네트워크 연결

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

uf = [-1] * (N+1)

def cmp(x, y):
    if x[2] < y[2]:
        return -1
    else: return 1

def find(x):
    if uf[x] < 0: return x
    uf[x] = find(uf[x])
    return uf[x]

def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    uf[x] = y

edges = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[2])

ans = 0
for u, v, cost in edges:
    if(find(u) == find(v)):
        continue
    merge(u, v)
    ans += cost

print(ans)