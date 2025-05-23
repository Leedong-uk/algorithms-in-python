from collections import deque

s = "[](){}"
correct = {"}": "{", "]": "[", ")": "("}
n = len(s)
cnt = 0

for i in range(n):
    stack = []
    rotated = s[i:] + s[:i]  

    for x in rotated:
        if x in "({[":
            stack.append(x)
        elif stack and stack[-1] == correct[x]:
            stack.pop()
        else:
            stack.append(x)

    if not stack:
        cnt += 1

print(cnt)
