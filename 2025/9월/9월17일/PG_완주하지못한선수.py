def solution(participant,completion):
    answer = ''
    total_score = 0
    dic = {}
    for i in participant : 
        print(i)
        total_score +=hash(i)
        dic[hash(i)] = i
    
    for i in completion : 
        total_score -= hash(i)
    
    answer = dic[total_score]
    return answer


print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))