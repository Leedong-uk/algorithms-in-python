input = input()
answer = ""
stack = []


for i in input : 
    if i.isalnum() : 
        answer += i
    
    elif i == "(" : 
        stack.append(i)
    
    elif i == "*" or i == "/" : 
        while stack and (stack[-1] == "*" or stack[-1] == "/") : 
            answer += stack.pop()
        stack.append(i)

    elif i == "+" or i == "-" : 
        while stack and stack[-1] !="(" : 
            answer += stack.pop() 
        stack.append(i) 

    elif i == ")" : 
        while stack and stack[-1] != "(" : 
            answer += stack.pop()
        stack.pop()
    

while stack : 
    answer += stack.pop()

print(answer)