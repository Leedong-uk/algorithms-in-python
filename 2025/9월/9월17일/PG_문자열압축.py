def solution(s):
    if len(s) == 1:
        return 1

    answer = len(s)  

    for i in range(1, len(s)//2 + 1):
        compressed = ""  
        prev = s[:i]    
        count = 1

        for j in range(i, len(s), i):
            cur = s[j:j+i]
            if cur == prev:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                prev = cur
                count = 1

        compressed += (str(count) + prev) if count > 1 else prev

        answer = min(answer, len(compressed))

    return answer


print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
