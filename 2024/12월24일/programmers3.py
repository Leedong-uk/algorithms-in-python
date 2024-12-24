s=")()("
temp = []

for i in s : 
    temp.append(i)

    if len(temp) >1 and temp[-1] ==')' and temp[-2] =='('  :
        temp.pop()
        temp.pop()


if temp : 
    answer = False
else : 
    answer = True

print(answer)
