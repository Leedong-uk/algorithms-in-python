from collections import deque
n = int(input())
check = [[-1]*(n+1) for _ in range(n+1)]
q = deque()
q.append((1,0))
check[1][0] = 0 

while q : 
    s,c = q.popleft()
    value = check[s][c]
    
    #1.(s,c) -> (s,c+s) ->클립보드로 복사 (덮어쓰기임)
    if (s+c <= n)and check[s][s] == -1 : 
        check[s][s] = value+1
        q.append((s,s))
    
    #2.(s,c)->(s+c,0) ->클립도으에 이모티콘 화면에 복사(클립보드 유지)
    if (s+c <= n) and check[s+c][c] == -1 : 
        check[s+c][c] = value +1
        q.append((s+c,c))
    
    #3.화면에 있는 이모티콘 삭제 (s,c) ->(s-1,c)
    if (0<s-1 <= n ) and check[s-1][c] == -1 : 
        check[s-1][c] = value +1
        q.append((s-1,c))

temp = check[n] 
min_value = float('inf')
for i in temp : 
    if i == -1 : 
        continue
    else : 
        result = min(min_value,i)
        min_value = result

print(result)
        
    
