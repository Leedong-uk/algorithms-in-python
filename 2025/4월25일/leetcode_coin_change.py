from collections import deque

coins = [1, 2, 5]
amount = 11
check = [-1] * (amount + 1)

q = deque()
check[0] = 0
q.append(0)

while q:
    current_amount = q.popleft()
    
    for coin in coins:
        next_amount = current_amount + coin
        if next_amount <= amount and check[next_amount] == -1:
            check[next_amount] = check[current_amount] + 1
            q.append(next_amount)

print(check[amount])
