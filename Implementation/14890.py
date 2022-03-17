# https://www.acmicpc.net/problem/14890
# 14890번 경사로

N, L = map(int, input().split())

board = [list(map(int, input().split())) for row in range(N)]

ans = 0

# check row 
for i in range(N):
    visited = [0 for row in range(N)]
    y, x = i, 0
    while x < N-1:
        isPossible = True
        curr = board[y][x]
        next = board[y][x+1]
        if next == curr:
            pass
        elif next > curr:
            if next - curr > 1:
                break

            # 깔수있나?
            for j in range(x-L+1, x+1):
                if x-L+1 < 0 or curr != board[y][j] or visited[j] > 0:
                    isPossible = False
                    break
            
            # 깔아버리기
            if isPossible:
                for j in range(x-L+1, x+1):
                    visited[j] = 1

        else:
            if curr - next > 1:
                break
        
            # 깔수있나?
            for j in range(x+1, x+L+1):
                if x+L >= N or next != board[y][j] or visited[j] > 0:
                    isPossible = False
                    break
            

            if isPossible:
                for j in range(x+1, x+L+1):
                    visited[j] = 1
            
        if isPossible:
            x += 1
        else:
            break
    
    if x == N-1:
        ans += 1

# down 
for i in range(N):
    visited = [0 for col in range(N)]
    y, x = 0, i
    while y < N-1:
        isPossible = True
        curr = board[y][x]
        next = board[y+1][x]
        if next == curr:
            pass
        elif next > curr:
            if next - curr > 1:
                break

            # 깔 수 있나?
            for j in range(y-L+1, y+1):
                if y-L+1 < 0 or curr != board[j][x] or visited[j] > 0:
                    isPossible = False
                    break
            
            # 깔아버리기
            if isPossible:
                for j in range(y-L+1, y+1):
                    visited[j] = 1

        else:
            if curr - next > 1:
                break

            # 깔 수 있나?
            for j in range(y+1, y+L+1):
                if y+L >= N or next != board[j][x] or visited[j] > 0:
                    isPossible = False
                    break
            
            # 깔아버리기
            if isPossible:
                for j in range(y+1, y+L+1):
                    visited[j] = 1
            
        if isPossible:
            y += 1
        else:
            break
    
    if y == N-1:
        ans += 1


print(ans)