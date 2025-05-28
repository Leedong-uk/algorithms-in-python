from collections import deque , defaultdict
def solution(id_list, report, k):
    answer = []
    unique_report = set(report)
    report_list = defaultdict(list)
    report_count = defaultdict(int)
    
    for i in unique_report : 
        sender , receiver = i.split()
        report_list[sender].append(receiver)
        report_count[receiver] +=1
    ban = set()
    
    for user,count in report_count.items() : 
        if count >= k : 
            ban.add(user)
    
    for i in id_list :
        cnt = 0
        for j in report_list[i] : 
            if j in ban : 
                cnt +=1
        answer.append(cnt)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))