# https://www.acmicpc.net/problem/1182
# 1182번 부분수열의 합

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

def dfs(idx, sum):
    if idx >= N:
        return 0

    ret = 0
    if sum + arr[idx] == S:
        ret += 1
    
    ret += dfs(idx+1, sum + arr[idx])
    ret += dfs(idx+1, sum)
    return ret

ans = dfs(0, 0)
print(ans)