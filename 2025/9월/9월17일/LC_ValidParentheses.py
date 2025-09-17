class Solution(object):
    def isValid(self, s):
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
        