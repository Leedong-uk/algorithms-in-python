def solution(a,b):
    answer = 0
    temp = 0 
    a.sort()
    b.sort(reverse =True)
    for i in range(len(a)) : 
        temp = a[i]*b[i]
        answer += temp
        
    return answer