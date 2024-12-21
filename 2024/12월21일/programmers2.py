n=5
lost = [2, 4]
reverse = [1, 3, 5]
people = [False] * (n+1)
answer = 0
for i in reverse : 
    people[i] = True

for i in lost : 
    if i in reverse : 
        people[i] = True 
        reverse.remove(i)
    else : 
        pre_val = i-1
        next_val = i+1
        if pre_val in reverse : 
            people[i] = True
            reverse.remove(pre_val)
        elif next_val in reverse : 
            people[i] = True
            reverse.remove(next_val)

answer = people.count(True)
print(answer)

입력값 〉 5, [4, 2], [3, 5]
기댓값 〉 5