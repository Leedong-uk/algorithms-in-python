#index 규칙
'''
root = i
left = i*2 +1
right = i*2 +2
parent = (i-1)/2
'''

#파이썬은 기본적으로 최소힙을 지원한다
#그냥 힙에 넣는것 만드오롣 힙정렬을 수행함 
'''heappush([자료를 저장할 자료구조] , 저장할것)'''
from heapq import heappush,heappop
heap = [] #그냥 list로 생성
li = [1,2,3,4,5]
for num in li : 
    heappush(heap,li)

'''heapppop([heap 자료구조] )'''
'''최소힙이니깐 가장 최소값이 출력됨'''
print(heappop(heap))


#max heap 만들기
from heapq import heappush,heappop
heap = []
li = [1,2,3,4,5]
for num in li : 
    heappush(heap,(-num,num))

print(heappop(heap)[1])

#n번쨰 최소 값 찾기
from heapq import nsmallest
'''nsamllest([작은값 몇개?],[어디서?(heap 아니여도 됨 list여도 가능)]])'''
li = [1,2,3,4,5]
min_li = nsmallest(3,li)
print(min_li) #-> 왼쪽부터 순서대로 첫번쨰,두번쨰,3번쨰 작은값

#n번쨰 큰 값 찾기
from heapq import nlargest
li = [1,2,3,4,5]
max_li = nlargest(3,li)
print(max_li) # -> 왼쪽부터 순서대로 첫번쨰,두번쨰,세번쨰 큰값 을가진 리스트

#힙에 단순히 넣었다 뻈다 하는것 만으로 힙정렬 구현해보자
from heapq import heappush,heappop

def heap_sort(li) : 
    heap = []
    temp = li[:] # 이렇게 한 이유는 원본 데이터는 유지하고 싶어서
    for num in temp :
        heappush(heap,num)
    
    result = []
    while heap : 
        result.append(heappop(heap))
    
    return result