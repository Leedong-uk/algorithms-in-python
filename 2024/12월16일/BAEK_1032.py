n = int(input())
temp = []


command = [input() for _ in range(n)]

result = list(command[0])
for i in range(len(command[0])) : 
    for j in range(n) : 
        if command[j][i] != result[i] : 
            result[i] = '?'
print("".join(result))

    