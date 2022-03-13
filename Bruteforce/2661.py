# https://www.acmicpc.net/problem/2661
# 2661번 좋은수열

N = int(input())

state = []

def dfs(idx):
    if idx >= N:
        return
    
    if idx == N-1:
        print(''.join(map(str, state)))
        exit()

    if idx == -1:
        for i in range(1, 4):
            state.append(i)
            dfs(idx+1)
            state.pop()
    
    for cand in [1, 2, 3]:
        isPossible = True
        max_size = (idx+1+1) // 2
        state.append(cand)

        for size in range(1, max_size+1):
            sub1 = state[idx-size+2:idx+2]
            sub2 = state[idx-size*2+2:idx-size+2]
            if sub1 == sub2:
                isPossible = False

        state.pop()

        if isPossible:
            state.append(cand)
            dfs(idx+1)
            state.pop()
    
dfs(-1)