'''
1.result 리스트 만들어서 []
2. 처음 값을 result 에 push 
3. result = [[1,3]]
4. 다음 2가 1,3 에 안들어 있거나 끝자리 3 과 같지 않다면 result[]에 push
5. 안들어 있으면 result[[1,3],[2,4]]
6. 그 다음 3 이 1,3에 안들어 있거나 끝자리가 같다면 result[0] update
7. result[[3,5],[2,4]]'''
import heapq
import sys

input = sys.stdin.readline
n = int(input())
temp = [tuple(map(int, input().split())) for _ in range(n)]
temp.sort() 

heap = []

heapq.heappush(heap,temp[0][1])


for i in range(1,n) : 
    start, end = temp[i]


    if heap[0] <= start : 
        heapq.heappop(heap)
    

    heapq.heappush(heap,end)

print(len(heap))