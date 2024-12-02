import sys
from collections import namedtuple
input = sys.stdin.readline
Meeting = namedtuple('Meeting', ['begin', 'end'])

n = int(input())
a = [Meeting(*map(int,input().split())) for _ in range(n)]
a.sort(key = lambda p : (p.end,p.begin)) #끝시간이 짧은 순서대로 정렬 , 같은게 있으면 시작시간이 짧은걸로 정렬
now = 0
ans = 0 

for p in a : 
    if now <= p.begin : 
        now = p.end
        ans +=1

print(ans)

