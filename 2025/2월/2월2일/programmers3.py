name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
answer = []
name_dic = {}
answer = []

for i in range(len(name)) : 
    name_dic[name[i]] = yearning[i]

for picture in photo :
    score = 0
    for people in picture : 
        if people in name_dic : 
            score += name_dic[people]
    answer.append(score)
print(answer)

