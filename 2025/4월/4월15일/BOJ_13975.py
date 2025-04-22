import heapq
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) : 
    k = int(input())
    numbers = list(map(int,input().split()))
    heapq.heapify(numbers)
    total = 0
    
    while len(numbers)>1 : 
        x = heapq.heappop(numbers)
        y = heapq.heappop(numbers)
        
        temp = x+y
        total += temp
        
        heapq.heappush(numbers,temp)
    
    print(total)

