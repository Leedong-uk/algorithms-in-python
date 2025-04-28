from collections import deque
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
linked_list = [[] for _ in range(n+1)]
group = [-1] *(n+1)
q= deque()

for i in vertex : 
    linked_list[i[0]].append(i[1]) 
    linked_list[i[1]].append(i[0]) 


group[1] = 0
q.append(1)

while q : 
    x= q.popleft()
    value = group[x]
    for i in linked_list[x] : 
        if group[i] == -1 : 
            group[i] = value+1
            q.append(i)
        

print(group.count(max(group)))
    
