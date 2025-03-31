import heapq
n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    heapq.heappush(heap, (-num, num))

while len(heap >1) : 
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    
    if x <0 or y<0 : 
        number = x *y 
    if x <= 1 or y<=1 : 
        number = x+y
        print ("x:",x,"y:",y,"number:",number,"(더하기)")
    else :
        number = x*y
        print ("x:",x,"y:",y,"number:",number,"(곱하기)")
        

print(heapq.heappop(heap)[1]) 
