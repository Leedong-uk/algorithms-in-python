from collections import deque
n = int(input())
a = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)

b = list(map(int,input().split()))
b = [x-1 for x in b]
order = [0]*n

for i in range(n):
    order[b[i]] = i

for i in range(n):
    a[i].sort(key=lambda x: order[x])
    #order의 원소순서대로 정렬을시킨다
    #그래서 이 오더 순서대로 dfs 알고리즘을 시행했을떄 성공한다면 이 접근방식은 맞게 되는것

dfs_order = []
check = [False]*n

def dfs(x):
    if check[x]:
        return
    dfs_order.append(x)
    check[x] = True
    for y in a[x]:
        dfs(y)

dfs(0)

ok = True
for i in range(n):
    if dfs_order[i] != b[i]:
        ok = False
print(1 if ok else 0)

