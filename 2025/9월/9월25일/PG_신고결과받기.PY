from collections import defaultdict
def solution(id_list,report,k) : 
    answer = []
    declaration_record = defaultdict(list)
    declaration_cnt = defaultdict(int)

    for id in id_list : 
        declaration_record[id] = []
        declaration_cnt[id] = 0
    
    for i in report : 
        sender,receiver = i.split()
        if receiver not in declaration_record[sender] : 
            declaration_record[sender].append(receiver)
            declaration_cnt[receiver] +=1
    
    for key ,value in declaration_record.items() : 
        cnt = 0 
        for id in value : 
            if declaration_cnt[id] >= k : 
                cnt +=1
        
        answer.append(cnt)
    return answer 


print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))