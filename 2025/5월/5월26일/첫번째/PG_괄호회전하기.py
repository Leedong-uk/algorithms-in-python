def solution(s):
    n = len(s)
    correct = {"}": "{", "]": "[", ")": "("}
    cnt = 0
    
    def start(rotate) : 
        stack = []
        for j in rotate : 
            if j in "{[(" : 
                stack.append(j)
            elif  stack and stack[-1] == correct[j] : 
                stack.pop()
            else : 
                return False
        return True 

    for i in range(n) : 
        rotate =list(s[i:] +s[:i]) 
        if start(rotate) : 
            cnt +=1
        # print(rotate)    

    return cnt



print(solution("[](){}"))
# solution("}]()[{")