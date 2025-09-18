def solution(s) : 
    answer = True
    q = list(s)
    que = []
    for i in q : 
        if i == "(" : 
            que.append(i)
            # print(que)
        elif que and que[-1] == "(" : 
            # print("q의 pop 발생",q)
            que.pop()
        else :
            return False
    
    if not que : 
        return True 
    else : 
        return False


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))