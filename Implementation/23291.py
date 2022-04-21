from collections import deque

def solution():
    global left, height, width, rolling
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # N, K = 100, 10
    # arr = list(i for i in range(1, 101))
    
    left = []

    rolling = [[0 for col in range(N)] for row in range(N)]
    height, width = 0, 0

    def is_valid(y, x, h, w):
        return (0 <= y < h and 0 <= x < w) and not rolling[y][x] == 0

    def min_add_one():
        arr_min = float('inf')
        arr_idx = []
        for i, val in enumerate(arr):
            if val <= arr_min:
                if val < arr_min:
                    arr_idx.clear()
                arr_idx.append(i)
                arr_min = val
        
        for i in arr_idx:
            arr[i] += 1

    def roll_1(idx, h, w):
        global left, height, width
        if idx+h > N:
            left = arr[idx:]
            height = h
            width = w
            for i in range(N-idx):
                rolling[h-1][w+i] = arr[idx+i]
            return

        row = [[0 for col in range(h)] for row in range(w)]
        for i in range(w):
            for j in range(h):
                row[i][j] = rolling[h-j-1][i]
        
        for i in range(w):
            for j in range(h):
                rolling[i][j] = row[i][j]

        for i in range(h):
            rolling[w][i] = arr[idx+i]
        
        if h > w:
            roll_1(idx+h, h, w+1)
        else:
            roll_1(idx+h, h+1, w)

    def control(h, w, left):
        lazy = [[0 for col in range(w+left+1)] for row in range(h+1)]

        for y in range(h):
            for x in range(w+left):
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if not is_valid(ny, nx, h, w+left): continue

                    diff = rolling[y][x] - rolling[ny][nx]

                    if diff >= 5:
                        lazy[y][x] -= diff//5
                        lazy[ny][nx] += diff//5
        
        for y in range(h):
            for x in range(w+left):
                rolling[y][x] += lazy[y][x]
    
    def straight(h):
        idx = 0
        j = 0
        w = 0
        k = 0
        while idx+j < N:
            if rolling[h-k-1][w] == 0:
                w += 1
                k = 0

            arr[idx+j] = rolling[h-k-1][w]
            
            if h-k-1 == 0:
                j = 0
                idx += h
                k = 0
                w += 1
            else:
                j += 1
                k += 1
        
    def roll_2(h, w, cnt):
        global height, width
        if cnt == 2:
            height = h
            width = w
            return

        row = [[0 for col in range(w)] for row in range(h*2)]

        for i in range(h-1, -1, -1):
            for j in range(w//2-1, -1, -1):
                row[h-i-1][w//2-j-1] = rolling[i][j]
        
        for i in range(0, h):
            for j in range(w//2, w):
                row[h+i][j-w//2] = rolling[i][j]
        
        for i in range(h*2):
            for j in range(w):
                rolling[i][j] = row[i][j]

        roll_2(h*2, w//2, cnt + 1)
    
    def go():
        global rolling, left, height, width
        height = 0
        width = 0
        left = []
        rolling = [[0 for col in range(N)] for row in range(N)]
        min_add_one()
        rolling[0][0] = arr[0]
        rolling[1][0] = arr[1]
        roll_1(2, 2, 1)
        control(height, width, len(left))
        straight(height)
        rolling = [[0 for col in range(N)] for row in range(N)]
        for i in range(N):
            rolling[0][i] = arr[i]
        roll_2(1, N, 0)
        control(height, width, 0)
        straight(height)

    def check():
        min_value = float('inf')
        max_value = 0
        for i in range(N):
            min_value = min(min_value, arr[i])
            max_value = max(max_value, arr[i])
        
        return max_value-min_value <= K

    ans = 0
    while check() == False:
        go()
        ans += 1
    
    print(ans)

solution()

'''
8 7
5 2 3 14 9 2 11 8

10 7
1 2 3 4 5 6 7 8 9 10

4 0
1 10000 1 10000

4 0
5602 5602 4400 4400

4 0
4929 5074 5074 4929

4 5
1 2 3 4

'''