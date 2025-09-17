def solution(prices) : 
    answer = []
    
    for i in range(len(prices)) : 
        temp = len(prices) -1
        for j in range(i,len(prices)) : 
            if prices[i] > prices[j] : 
                temp = j
                break
        
        answer.append(temp-i)

    return answer 



print(solution([1,2,3,2,3]))