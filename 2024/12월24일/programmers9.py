from collections import deque
def solution(s):
    s = deque(s)
    temp = []
    
    
    while s:
        temp_val = s.popleft()
        if temp : 
            if temp[-1] != temp_val: 
                temp.append(temp_val)
            else : 
                temp.pop()
        else:
            temp.append(temp_val)
            
        

    if temp :
        answer = 0
    else : 
        answer = 1
    return answer