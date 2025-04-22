temperatures = [73,74,75,71,69,72,76,73]
n=len(temperatures)
result = [0]*n
stack =[]

for current_index in range(len(temperatures)) : 
    current_value = temperatures[current_index]
    while stack and current_value > temperatures[stack[-1]] : 
        stack_index= stack.pop()
        result[stack_index] = current_index - stack_index
    stack.append(current_index)

while stack : 
    index = stack.pop()
    result[index] = 0
print(result)
    