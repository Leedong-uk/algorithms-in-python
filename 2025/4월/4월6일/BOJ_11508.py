import heapq
n = int(input())
num = []
result = 0

for _ in range(n) : 
    num.append(int(input()))

num.sort(reverse=True)

for i in range(0,len(num),3) : 
    if i+2 <= len(num)-1 : 
        result += sum(num[i:i+2])
    else : 
        result += sum(num[i:])

print(result)