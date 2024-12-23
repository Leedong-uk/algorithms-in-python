#누가 신고했는지 나타내는 배열
#누가 신고 몇번 당했는지 나타내는 배열 

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
result = []

reporter_check_dic = {}
check_dic = {}
index = 0
result = [0]*(len(id_list))
for i in id_list :
    reporter_check_dic[i] = []
    check_dic[i] = 0

for i in report : 
    reporter , people = i.split()
    if people not in reporter_check_dic[reporter] : 
        reporter_check_dic[reporter].append(people)
        check_dic[people] +=1

for i in reporter_check_dic :
    for people in reporter_check_dic[i] : 
        if check_dic[people] >= k : 
            result[index] +=1

    index+=1
 
print(result)