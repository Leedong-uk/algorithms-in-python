import sys
input = sys.stdin.readline

def flip(x):
    if x == 'H':
        return 'T'
    else:
        return 'H'

n = int(input())
a = [input() for _ in range(n)]
ans = n*n

for state in range(1<<n): #비트마스크를 이용해서 각 행에 대해서 선택할지 말지를 부분집합으로 나타냄
    tot = 0
    for j in range(n): #각 열에 대해서 하나하나 보면서
        cnt = 0
        for i in range(n): #각 열해 i번쨰 행에대해서
            cur = a[i][j]
            if (state & (1 << i)) != 0: #그 행이 현재 부분집합state에서 뒤집어야하는지(1) 아닌지(0)를 파악하고
                cur = flip(cur) #뒤집어야한다면 뒤집음
            if cur == 'T': #그 열에 대해서 모든 t값을 가져옴
                cnt += 1
        tot += min(cnt, n-cnt) #이렇게 전체 진행하고 지금 값(처음에 선택한것) 처음에 선택하지 않은 값중 최소값을 가져옴
    if ans > tot:
        ans = tot
print(ans)