def solution(s) : 
    answer = 0 
    correct = {"}":"{" , "]":"[" , ")":"("} 
    
    for i in range(len(s)) : 
        rotate = s[i:] + s[:i]
        stack = []
        for j in rotate : 
            if j in "{[(" : 
                stack.append(j)
            elif stack  and correct[j] == stack[-1] : 
                stack.pop()
            elif not stack : 
                stack.append(j)
        
        if not stack : 
            answer +=1
                
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))