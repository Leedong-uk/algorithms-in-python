#기본적인 알고리즘 : 가방과 보석을 하나의 자료구조에 저장하고
#가방이 나올떄까지 보석을 후보에 넣고 가방이 나오면 
#후보에 넣었던 보석중 가장 가치가 큰 애를 뽑으면 된다 
#이떄 뽑을떄 필요한게 max heap 자료형
import sys
from collections import namedtuple
from heapq import heappush, heappop
input = sys.stdin.readline
Jewel = namedtuple('lecture', ['m', 'v', 'w']) # 무게 , 가치 , 보석 :0 가방 : 1

n , k = map (int,input().split())
a = []
for _ in range(n) :# 보석 : 0
    m , v = map(int,input().split())
    a.append(Jewel(m,v,0))

for _ in range(k) : #가방 : 1
    m = int(input())
    a.append(Jewel(m,0,1))

a.sort(key=lambda p: (p.m, p.w))
q= [] #후보 = max heap
ans = 0 

for p in a : 
    if p.w == 0 : 
        heappush(q,-p.v)
    
    else : 
        if q : 
            ans += -heappop(q)
print(ans)


