from collections import deque , defaultdict
def solution(id_list, report, k):
    result = []
    unique_report = set(report)
    report_dic = defaultdict(list)
    report_count = defaultdict(int)
    
    for i in unique_report : 
        sender , receiver = i.split() 
        report_dic[sender].append(receiver)
        report_count[receiver] +=1
    
    
    
    
    ban = set()
    
    for user , count in report_count.items() : 
        if count >= k : 
            ban.add(user)
    
    for user in id_list : 
        cnt = 0 
        for target in report_dic[user] : 
            if target in ban : 
                cnt +=1
        result.append(cnt)
            
    
    return result

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))
