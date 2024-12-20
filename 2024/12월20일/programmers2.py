lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
check =0
zero_check=0
max_rank = 0
min_rank = 0
result = [6,6]
money = {6:1,5:2,4:3,3:4,2:5}


for i in win_nums : 
    if i in lottos : 
        lottos.remove(i)
        check +=1
zero_check = lottos.count(0)

max_rank = zero_check + check
min_rank = check

if max_rank in money : 
    result[0] = money[max_rank]

if min_rank in money : 
    result[1] = money[min_rank]

print(result)
   


        