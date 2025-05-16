from collections import deque
from copy import deepcopy

n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
linked_list = [[] for _ in range(n+1)]  

for x, y in wires:
    linked_list[x].append(y)
    linked_list[y].append(x)

def bfs(linked_list, start):
    check = [False] * (n + 1)
    q = deque()
    cnt = 1
    check[start] = True
    q.append(start)

    while q:
        x = q.popleft()
        for i in linked_list[x]:
            if not check[i]:
                cnt += 1
                check[i] = True
                q.append(i)
    return cnt

def cut_wire(linked_list, x, y):
    linked_list[x].remove(y)
    linked_list[y].remove(x)
    return linked_list

def find_result(linked_list, n):
    min_diff = n 
    for x, y in wires:
        temp_board = deepcopy(linked_list)
        cut_board = cut_wire(temp_board, x, y)
        count = bfs(cut_board, x)  
        diff = abs(count - (n - count))
        min_diff = min(min_diff, diff)
    return min_diff


print(find_result(linked_list, n)) 
