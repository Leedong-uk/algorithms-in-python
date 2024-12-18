n = int(input())
T = [0]*(n+1)
Y = [0]*(n+1)
money = 0
day = 0
i = 0
result = []

for i in range(1,n+1) : 
    t , y = map(int,input().split())
    T[i] = t
    Y[i] = y

while True : 

    if  i == n : 
        break

    day = T[i]
    money = Y[i]

    while day <= n and day + T[day] <=n  : 
        money +=Y[day]
        day +=T[day] 

    result.append(money)
    i +=1


print(result)
        




