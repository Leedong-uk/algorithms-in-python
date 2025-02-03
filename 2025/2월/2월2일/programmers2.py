cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
check = False

for i in goal : 
    if cards1 and i == cards1[0] : 
        cards1.pop(0)
    elif cards2 and i == cards2[0] : 
        cards2.pop(0)
    else : 
        check = True
        break

if check : 
    print("No")
else : 
    print("Yes")