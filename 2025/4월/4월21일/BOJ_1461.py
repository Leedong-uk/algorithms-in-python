n , m  = map(int,input().split())
number = list(map(int,input().split()))
plus= sorted([i for i in number if i>0],reverse=True)
minus= sorted([abs(i) for i in number if i <0],reverse=True)

distance = []

for i in range(0,len(plus),m) : 
    distance.append(plus[i])
    
for i in range(0,len(minus),m) : 
    distance.append(minus[i])
    
distance.sort()
result = distance.pop()

for i in distance : 
    result += i*2

print(result)
