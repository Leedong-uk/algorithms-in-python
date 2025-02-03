cacheSize = 2
answer = 0
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
cache = []

for i in cities : 
    if i in cache :
        cache.remove(i)
        cache.append(i)
        answer +=1
    else : 
        if len(cache) >= cacheSize : 
            cache.pop(0)
        cache.append(i)
        answer +=5

print(answer)
