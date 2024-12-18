food = list(map(int,input().split()))
n = list(map(lambda x : x//2 , food))
result = [] 

for index in range(1,len(food)) : 
    if index == 1 :
        result.append((str(index))*(n[index]*2))
    else : 
        l = 0
        r = len(result)
        m = (l+r) // 2
        result.insert(m,(str(index))*(n[index]*2))


print(result)
