want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
want_dic = {}
check_dic = {}
check = True 
answer = 0

for i in range(len(want)) : 
    want_dic[want[i]] = number[i]
    check_dic[want[i]] = 0

init = check_dic.copy()

for i in range(len(discount)-9) : 
    check_dic = init.copy()

    for j in range(i,i+10) :
        if discount[j] in want : 
            check_dic[discount[j]] +=1

    if check_dic == want_dic : 
        answer = i
        break

    
print(answer)
    


        

def solution(want, number, discount):
    answer = 0
    want_dic = {}
    check_dic = {}
    
    for i in range(len(want)) : 
        want_dic[want[i]] = number[i]
        check_dic[want[i]] = 0

    init = check_dic.copy()

    for i in range(len(discount)-9) : 
        check_dic = init.copy()

        for j in range(i,i+10) :
            if discount[j] in want : 
                check_dic[discount[j]] +=1

        if check_dic == want_dic : 
            answer = i+1
            break
            
    return answer