#양수는 양수끼리 음수는 음수 끼리 묶어야함 
#양수는 큰수끼리
#음수는 작은수끼리 묵어야 좋다 
#음수끼리 못묶을떄(개수가 홀수) 일떄 음수 *0을 묶어서 음수를 지워버리는것도 있음
#ㄴ음수의 개수 판단
#ㄴ0의 존재 유무 판단 
#1이랑 묶이는건 의미가 없음

import sys
input = sys.stdin.readline
n = int(input())
plus = []
minus = []
zero = 0
one = 0

for _ in range(n):
    x = int(input())
    if x == 1:
        one += 1
    elif x > 0:
        plus += [x]
    elif x < 0:
        minus += [x]
    else:
        zero += 1

plus.sort()
minus.sort()
plus.reverse()

if len(plus) % 2 == 1:
    plus += [1]

if len(minus) % 2 == 1:
    minus += [0 if zero > 0 else 1]

ans = one
for i in range(0, len(plus), 2):
    ans += plus[i] * plus[i+1]
    
for i in range(0, len(minus), 2):
    ans += minus[i] * minus[i+1]
print(ans)

