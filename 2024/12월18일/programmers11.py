def solution(babbling):
    can_s = ['aya','ye','woo','ma']
    cant_s = ['ayaaya','yeye','woowoo','mama']
    cnt = 0
    
    for word in babbling:
        
        for i in cant_s : 
            if i in word : word = word.replace(i,'x')
        for i in can_s : 
            if i in word : word = word.replace(i,' ')
        
        word = word.replace(' ','')
        if word == '' : cnt += 1
        
    return cnt