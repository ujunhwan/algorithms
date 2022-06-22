import heapq
import sys
input = sys.stdin.readline

N = int(input())

left = []
right = []

for _ in range(N):
    num = int(input())
    if len(left) > 0 and -left[0] < num:
        heapq.heappush(right, num)
    else:
        heapq.heappush(left, -num)
    
    if len(left) > len(right)+1:
        top = heapq.heappop(left)
        heapq.heappush(right, -top)
    elif len(left) < len(right):
        top = heapq.heappop(right)
        heapq.heappush(left, -top)
    
    print(-left[0])
