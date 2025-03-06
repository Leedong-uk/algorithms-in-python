participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

dic = {}
total_hash = 0
for i in participant : 
    dic[hash(i)] = i
    total_hash += hash(i)


for i in completion : 
    total_hash -= hash(i)

answer = dic[total_hash]
print(answer)
