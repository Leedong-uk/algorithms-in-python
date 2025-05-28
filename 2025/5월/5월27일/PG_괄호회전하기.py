def solution(s) : 
    answer = 0 
    
    cnt = 0
    correct = {"}":"{" , "]":"[" , ")":"("}  
    for i in range(len(s)) : 
        rotate = s[i:]+s[:i]
        stack = []
        for j in rotate : 
            if j in "{[(" : 
                stack.append(j)
            elif stack and stack[-1] == correct[j] : 
                stack.pop()
            elif not stack : 
                stack.append(j)
        if not stack : 
            cnt +=1
    return cnt 

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))