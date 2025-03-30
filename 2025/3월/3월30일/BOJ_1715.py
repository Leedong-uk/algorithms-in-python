import heapq
import sys

input = sys.stdin.readline
n = int(input())

heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)  

result = 0

while heap:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    cur = x + y 
    heapq.heappush(heap, cur) 
    result += cur 
    

print(result)
