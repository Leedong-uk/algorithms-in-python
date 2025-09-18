from collections import deque

def canVisitAllRoomx(rooms) : 
    q = deque()
    n = len(rooms)
    visited = [False] * n 
    
    visited [0] = True 
    q.append(0)
    
    while q : 
        x = q.popleft()
        for key in rooms[x] : 
            if not visited[key] : 
                visited[key] = True
                q.append(key)
    
    
    if False not in visited : 
        return True 
    else : 
        return False
        
    