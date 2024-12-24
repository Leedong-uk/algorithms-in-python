def solution(people, limit):
    people.sort(reverse = True)
    total = 0
    cnt = 0
    
    for i in people : 
        total = i
        if total + people[-1] <= limit : 
            people.pop()
            cnt +=1
        else : 
            cnt +=1

    return cnt