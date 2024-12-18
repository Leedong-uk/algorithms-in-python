cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
i = 0
result = []
while i != len(goal) : 
    if cards1 == False or cards2 == False : 
        break
    if cards1[0] == goal[i] : 
        x = cards1.pop(0)
        result.append(x)
    elif cards2[0] == goal[i] : 
        x = cards2.pop(0)
        result.append(x)
    
    i +=1


if cards1 : 
    for i in cards1 :
        result.append(i)

if cards2 : 
    for i in cards2 : 
        result.append(i)

if goal == result :
    print("Yes") 
else : 
    print("No")