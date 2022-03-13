# https://www.acmicpc.net/problem/1759
# 1759번 암호 만들기

import sys
input = sys.stdin.readline

L, C = map(int, input().split())
arr = sorted(list(input().split()), key=lambda x: ord(x))

vowels = ['a', 'e', 'i', 'o', 'u']

def dfs(idx, a, b, state):
    # a 자음 b 모음 

    if a+b == L:
        if a >= 2 and b >= 1:
            print(state)
        return

    if idx >= C:
        return
    
    if arr[idx] in vowels:
        dfs(idx+1, a, b+1, (state+arr[idx]))
        dfs(idx+1, a, b, state)
    else:
        dfs(idx+1, a+1, b, (state+arr[idx]))
        dfs(idx+1, a, b, state)

dfs(0, 0, 0, "")