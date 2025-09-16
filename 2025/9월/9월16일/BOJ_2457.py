n = list(map(lambda x: x**2, map(int, input().split())))
result = 0 
for i in n : 
    result += i

print(result%10)