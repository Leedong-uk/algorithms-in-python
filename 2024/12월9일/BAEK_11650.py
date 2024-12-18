n = int(input())
number =[]
for _ in range(n) : 
    x,y = map(int,input().split())
    number.append((x,y))

number.sort(key = lambda x : (x[0],x[1]))

for i in range(n) : 
    print(number[i][0],number[i][1])

    