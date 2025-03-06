numbers = [2, 3, 3, 5]
result = [-1]*len(numbers)
stack = []

stack.append(0)
for i in range(1,len(numbers)) :
    current_val = numbers[i]
    while len(stack) >= 1 and current_val > numbers[stack[-1]]  :
        x = stack.pop(-1)
        result[x] = current_val
    stack.append(i)
    print('i가',i,'일떄 끝난후 stack 상황 : ',stack)

print(result)    
        
    
