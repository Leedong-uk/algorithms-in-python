from heapq import *
scoville = [1, 2, 3, 9, 10, 12]
k = 7
heapify(scoville)
cnt = 0


while len(scoville) >=2 : 
    if scoville[0] >= k :
        break
    
    min_li = nsmallest(2,scoville)
    new_food = min_li[0] + (2*min_li[-1])
    
    for _ in range(2) : 
        heappop(scoville)
    
    heappush(scoville,new_food)
    cnt +=1

else : 
    cnt = -1
    
print(cnt)
    