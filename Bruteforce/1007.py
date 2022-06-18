from itertools import combinations
import sys
input = sys.stdin.readline

T = int(input())

INF = 9876543210

for tc in range(T):
    ans = INF
    totalY, totalX = 0, 0
    arr = list()
    N = int(input())
    for i in range(N):
        pos = list(map(int, input().split()))
        arr.append(pos)
        totalY += pos[0]
        totalX += pos[1]

    for comb in combinations(arr, N//2):
        sumY, sumX = 0, 0
        for y, x in comb:
            sumY += y
            sumX += x
        
        yy = totalY - 2 * sumY
        xx = totalX - 2 * sumX

        ans = min(ans, (yy ** 2 + xx ** 2)**(1/2))
    
    print(ans)



'''
1
2
-100000 -100000
100000 100000

1
4
5 5
5 -5
-5 5
-5 -5

1
6
1 1
2 2
5 5
5 -5
-5 5
-5 -5
'''
