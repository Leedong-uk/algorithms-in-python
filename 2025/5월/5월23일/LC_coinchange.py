from collections import deque
coins = [1,2,5]
amount = 11
check = [-1] * (amount+1)
q = deque()

check[0] = 0
q.append(0)


while q : 
    money = q.popleft()
    cnt = 0
    for coin in coins : 
        change_money = coin+money
        if change_money<=amount and check[change_money] == -1 : 
            check[change_money] = check[money]+1
            q.append(change_money)

print(check[amount])