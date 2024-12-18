n = int(input())
day = 0
check = 0 
for _ in range(n) : 
    x = input()
    day = int(x[2:])

    if day <=90 : 
        check +=1


print(check)