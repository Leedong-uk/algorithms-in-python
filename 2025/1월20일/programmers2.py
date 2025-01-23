from collections import deque
q = deque()
priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = []

for i in range(len(priorities)) : 
    q.append(i)

while q : 
    temp = q.popleft()
    
    if any(priorities[temp]<priorities[i] for i in q): 
        q.append(temp)
    else :
        answer.append(temp)
        if temp == location : 
            break
print(len(answer))
