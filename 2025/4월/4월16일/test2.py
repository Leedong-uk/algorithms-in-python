prices = [1, 2, 3, 2, 3]
result = [0] * len(prices)
stack = []

for current_index in range(len(prices)) :
    current_value = prices[current_index]
    while stack and current_value < stack[-1] : 
        stack_index = stack.pop()
        result[stack_index] = current_index - stack_index
    stack.append(current_index)

while stack : 
    index = stack.pop()
    result[index] = len(prices) - index - 1
    