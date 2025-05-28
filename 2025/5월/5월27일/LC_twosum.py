def solution(num , target) : 
    answer = []
    num_dic = {}
    for i ,num in enumerate(num) : 
        num_dic[num] = i
        complement = target -num 
        if complement in num_dic : 
            return [num_dic[complement],i]
        
    return answer

print(solution([2,7,11,15],9))
print(solution([3,2,4],6))