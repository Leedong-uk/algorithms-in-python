#n : 숫자의 개수를 입력받음 (index가 될꺼임)
#

import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
check = [False]*n
ans = [0]*m

def go(index, n, m):
    if index == m:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        ans[index] = num[i]
        go(index+1, n, m)
        check[i] = False

go(0,n,m)