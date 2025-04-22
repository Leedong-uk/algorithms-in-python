def is_valid_bracket(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for i in s:
        if i in bracket_map:  
            if stack and stack[-1] == bracket_map[i]:
                stack.pop()
            else:
                return False
        else:  
            stack.append(i)

    return len(stack) == 0  


# 예제 실행
print(is_valid_bracket("([])"))  
print(is_valid_bracket("([)]"))  
print(is_valid_bracket("((()))"))  
