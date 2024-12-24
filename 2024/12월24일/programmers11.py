def solution(arr):
    answer = 0
    
    def gcm (a,b) : 
        while b>0 :
            a,b = b,a%b
        return a
    
    def lcm (a,b) : 
        return a*b/gcm(a,b)
    
    temp = lcm(arr[0],arr[1])
    for i in range(2,len(arr)) : 
        temp = lcm(temp,arr[i])
    
    answer = temp
    return answer
