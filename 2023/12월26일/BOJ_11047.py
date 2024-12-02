n , k = map(int,input().split())
money = [0]*n
ans = 0 

for i in range(n) : 
    x = int(input())
    money[i] = x

money.reverse()

for j in money : 
    ans += k//j
    k %= j

print(ans)
