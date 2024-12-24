def solution (n) : 
    while n>0 : 
        answer += n %2
        n = n//2
    return answer
