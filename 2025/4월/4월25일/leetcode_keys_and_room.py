from collections import deque
rooms = [[1],[2],[3],[]]
n = len(rooms)
q = deque()
check = [False] *n

check[0] = True
q.append(0)

while q : 
    x = q.popleft()
    for i in rooms[x] : 
        if check[i] == False : 
            check[i] = True
            q.append(i)
            
if False in check :
    print ("False")
else : 
    print("True")
    
    
