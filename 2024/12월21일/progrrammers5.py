#빵 – 야채 – 고기 - 빵 1 2 3 1
ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
result = 0
stack = []
check = []

for i in ingredient : 
    stack.append(i)
    if len(stack) >=4 and stack[-1] == 1 : 
        if stack[-1:-5:-1] ==[1,3,2,1] : 
            result +=1
            del stack[-1:-5:-1]

print(result)




