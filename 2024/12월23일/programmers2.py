bandage = [1, 1, 1]
health = 5
attacks = [[1, 2], [3, 2]]
attacks_info = {}
for i in attacks:
    attacks_info [i[0]] = i[1]
end_time = max(attacks_info)
current_time = 1
check_bandage = 0
attack_try = False

while current_time <= end_time : 
    if current_time not in attacks_info : 
        check_bandage +=1
        health += bandage[1]
        attack_try = False
        if health >30 :
            health = 30
    
        if check_bandage == bandage[0] :
            health += bandage[2]
            check_bandage = 0
            if health > 30 :
                health = 30
    else : 
        attack_try = True
        health -= attacks_info[current_time]
        check_bandage = 0

        if health <=0 : 
            health = -1
            break
    print("current_time :",current_time,"health :",health,"연속성공:",check_bandage,"공격시도",attack_try)
    current_time +=1

print(health)

입력값 〉 [1, 1, 1], 20, [[1, 5], [4, 1]]
기댓값 〉 18