id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
score= {}
check = {}
index = 0
result = [0]*(len(id_list))



for i in id_list :
    check[i] = []
    score[i] = 0

for i in report : 
    reporter , people = i.split()
    if people not in check[reporter] : 
        check[reporter].append(people)
        score[people] +=1

        
for i in check : 
    for name in check[i] : 
        if score[name] >= k : 
            result[index] +=1
    index+=1
print(result)