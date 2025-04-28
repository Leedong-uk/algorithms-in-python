from collections import deque
import sys
input = sys.stdin.read
data = input().split()

n, m = map(int, data[0:2])
linked_list = [[] for _ in range(n+1)]
result = [0] * (n+1)

index = 2
for _ in range(m):
    x, y = int(data[index]), int(data[index+1])
    linked_list[y].append(x)  # y -> x 방향 저장 (방향 주의)
    index += 2

def bfs(start):
    visited = [False] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = True
    cnt = 1

    while q:
        x = q.popleft()
        for i in linked_list[x]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)
    
    return cnt

max_value = -1
answer = []

for i in range(1, n+1):
    cnt = bfs(i)
    if cnt > max_value:
        max_value = cnt
        answer = [i]
    elif cnt == max_value:
        answer.append(i)

print(*answer)
