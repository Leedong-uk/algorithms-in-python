def solution(s):
    answer = ''
    answer_list = list(map(int,s.split()))
    answer += str(min(answer_list))
    answer += " "
    answer += str(max(answer_list))
    
    
    return answer