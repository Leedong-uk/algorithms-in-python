import ast
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = s.replace("{","[").replace("}","]")
s = ast.literal_eval(s)
s.sort(key = lambda x : len(x))
answer = []

for i in s : 
    for j in i :
        if j not in answer:
            answer.append(j)
print(answer)

