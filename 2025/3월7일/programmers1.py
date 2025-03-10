number = [1,2,3,1,2,3,4]

k = 3
result=""
stack = []
cnt = 0

for i in range(len(number)):    
    while stack and stack[-1] < number[i] and cnt < k : 
        stack.pop()
        cnt +=1
    stack.append(number[i])
    
while cnt <k : 
    stack.pop()
    cnt+=1

result = ''.join(list(map(str,stack)))
print(result)
    