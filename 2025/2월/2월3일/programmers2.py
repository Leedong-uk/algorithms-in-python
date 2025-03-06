#실패율 = 스테이지에 도달했으나 아직 클리어 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
#전체 스테이지 개수 = n 
#사용자가 현재 멈춰있는 스테이지 = stages
#실패율이 높은 스테이지 부터 내림차순으로  번호가 담겨있는 배열 return
from collections import Counter
n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
dic = Counter(stages)
total_players = len(stages)
fail_rates = []

for i in range((n+1)) : 
    if total_players > 0 : 
        fail = dic[i]/total_players
        total_players -= dic[i]
    else : 
        fail = 0
    
    fail_rates.append((i, fail))

fail_rates.sort(key=lambda x: (-x[1], x[0]))
print(fail_rates)





