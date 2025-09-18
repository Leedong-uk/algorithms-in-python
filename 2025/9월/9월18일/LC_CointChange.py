from collections import deque
def coinChange(coins,amount) : 
    visited = [-1] * (amount*2)
    q = deque()
    answer = 0
    
    q.append(0)
    visited[0] = 0
    
    while q : 
        x= q.popleft()
        if x == amount : 
            break
        for i in range(len(coins)) : 
            nx = x + coins[i]
            if  visited[nx] == -1 : 
                visited[nx] = visited[x] + 1
                q.append(nx)
    
    return visited[amount]


print(coinChange([1,2,5],11))