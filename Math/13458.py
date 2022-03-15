# https://www.acmicpc.net/problem/13458
# 13458번 시험 감독

import sys
from math import ceil
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N
for i in range(N):
    left = arr[i] - B
    if left <= 0:
        continue
    div, mod = divmod(left, C)
    div = div+1 if mod > 0 else div
    ans += div

print(ans)
