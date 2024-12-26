def solution(elements):
    answer = 0
    result = []
    size = 1
    index = 0
    total = len(elements)
    result.append(sum(elements))
    cnt = 0
    
    while True : 
        if size == len(elements) : 
            break
        start = index % total
        end = (index+size)% total
        
        if end <start : 
            x = elements[:end] + elements[start:]
        else :
            x = elements[start:end]
        
        if cnt == len(elements) :
            size +=1
            cnt = 0
        
        result.append(sum(x))
        index +=1
        cnt +=1
    
    return len(set(result))

