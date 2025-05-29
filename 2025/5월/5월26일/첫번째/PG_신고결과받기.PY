from collections import defaultdict
def solution(id_list, report, k):
    report_list = defaultdict(list)
    report_count = defaultdict(int)
    reporter = set(report)
    answer=[]
    
    for i in reporter : 
        sender , receiver = i.split()
        report_list[sender].append(receiver)
        report_count[receiver] +=1
    


    ban = set()

    for user , count in report_count.items() :
        # print("user : ",user ,",","count : ",count)
        if count >=k : 
            # print("정지 유저 발견 : ",user)
            ban.add(user)
            
    # print("ban 리스트 :",ban)
    # print("신고 이력 : ",report_list)
    for i in id_list : 
        cnt = 0 
        for j in report_list[i] : 
            if j in ban : 
                cnt +=1
        answer.append(cnt)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))
