name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
friend = {}
answer = []

for i in range(len(name)) : 
    friend[name[i]] = yearning[i]

key_friend = list(friend.keys())


for sets in photo : 
    result =0
    for j in sets : 
        if j in key_friend : 
            result += friend[j]
    answer.append(result)
    

    
print(answer)


    