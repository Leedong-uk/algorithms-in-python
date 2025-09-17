def dailyTemperature(temperatures) :
    stack = []
    answer = [0] * len(temperatures)
    for i in range(len(temperatures)) : 
        while stack and temperatures[stack[-1]] < temperatures[i] : 
            target_idx = stack.pop()
            answer[target_idx] = i - target_idx
        stack.append(i)
    
    while stack : 
        idx = stack.pop()
        answer[idx] = 0
    return answer


print(dailyTemperature([73,74,75,71,69,72,76,73]))
print(dailyTemperature([30,40,50,60]))
print(dailyTemperature([30,60,90]))