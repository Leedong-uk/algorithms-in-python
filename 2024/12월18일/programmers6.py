def solution(k, m, score):
    answer = 0
    result = 0
    n = len(score) // m 
    apple = sorted(score,reverse=True)
    k = 0
    
    for _ in range(n) : 
        
        result += min(apple[k:k+m])
        k = k+m
        
    
    answer = result *m
    return answer