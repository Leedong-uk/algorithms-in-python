from collections import Counter

def solution(want, number, discount):
    cnt = 0
    want_dic = Counter({want[i]: number[i] for i in range(len(want))})
    window = Counter(discount[:10])
    
    
    if not (want_dic - window):
        cnt += 1
    
    
    for i in range(10, len(discount)):
        
        window[discount[i]] += 1
        window[discount[i-10]] -= 1
        if window[discount[i-10]] == 0:
            del window[discount[i-10]]
        
        
        if not (want_dic - window):
            cnt += 1
    
    return cnt
