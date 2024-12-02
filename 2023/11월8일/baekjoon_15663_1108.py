#시간초과 떴음
"""n , m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
tmp = []
check = [False] * n
ans = [0] *m

def go (index,n,m) : 
    if index == m : 
        if tmp : 
            n = " ".join(map(str,ans))
            if n not in tmp : 
                tmp.append(n)
                return
            else :
                return
        
        else: 
            tmp.append(" ".join(map(str,ans)))
            return
    
    for i in range(n) : 
        if check[i]:
            continue
        check[i] = True
        ans[index] = num[i]
        go(index+1,n,m)
        check[i] = False


go(0,n,m)
for i in tmp : 
    print(i)
"""
#문자열 정렬은 사전 정렬과 다를수 있다
#따라서 튜플을 이용해 한쌍을 묶어주고 그거 자체를 정렬해야한다

n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
check = [False]*n
ans = [0]*m
tmp = []
def go(index, n, m):
    if index == m:
        tmp.append(tuple(ans))
        return
    
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        ans[index] = num[i]
        go(index+1, n, m)
        check[i] = False

go(0,n,m)
tmp = list(set(tmp))
tmp.sort()

for i in tmp: 
    print(" ".join(map(str,i)))

"""
#튜플로 쌍을 묶어서 그거 자체를 set,정렬 진행
import sys
n,m = map(int,input().split())
c = [False] * (n+1)
num = list(map(int,input().split()))
num.sort()
a = [0]*m
d = []
def go(index, n, m):
    if index == m:
        temp = [num[a[i]] for i in range(m)]
        print("temp = ",end=" ")
        print(temp)
        d.append(tuple(temp))
        print("d = ",end = " ")
        print(d)
        return
    for i in range(n):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, n, m)
        c[i] = False

go(0,n,m)
d = list(set(d))
d.sort()
for v in d:
    print(' '.join(map(str,v)))"""