# https://www.acmicpc.net/problem/10597
# 10597번 순열장난

import sys
input = sys.stdin.readline

str = input().rstrip()
N = len(str)
max_num = (N+9) // 2 if N >= 10 else N
visited = [0] * (max_num+1)

ans = []

def dfs(idx, state):
    global ans, visited, max_num

    if idx == N:
        for i in state:
            print(i)
        exit()

    if idx < N:
        next_num = int(str[idx])

        if next_num > max_num:
            return
        
        if not visited[next_num]:
            state.append(next_num)
            visited[next_num] = 1
            dfs(idx+1, state)
            state.remove(next_num)
            visited[next_num] = 0

    if idx+1 < N:
        next_num = int(str[idx]+str[idx+1])

        if next_num > max_num:
            return

        if not visited[next_num]:
            state.append(next_num)
            visited[next_num] = 1
            dfs(idx+2, state)
            state.remove(next_num)
            visited[next_num] = 0

dfs(0, [])