keymap = ["AGZ", "BSSS"]
targets = ["ASA","BGZ"]
dic = {}
answer = []

for i in keymap : 
    for j in range(len(i)) : 
        if i[j] not in dic : 
            dic[i[j]] = j+1
        else : 
            dic[i[j]] = min(dic[i[j]],j+1)

for i in targets : 
    temp = 0
    for j in i : 
        if j in dic : 
            temp += dic[j]
        else : 
            temp = -1
            break

    answer.append(temp)

print(answer)
            