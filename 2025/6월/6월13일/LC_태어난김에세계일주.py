balance = 600
countries = [[70, 350], [100, 550], [350, 400]]
check = [False]*len(countries)

def dfs(balance,cnt) :
    max_count = cnt
    
    if balance <= 0 :
        return max_count
    
    for i in range(len(countries)) : 
        if not check[i] and countries[i][1]<= balance:
            check[i] = True
            max_count = max(max_count,dfs(balance-countries[i][0],cnt+1))
            check[i] = False
    
    return max_count
print(dfs(balance,0))
             

# balance = 600
# countries = [[70, 350], [100, 550], [350, 400]]
# check = [False] * len(countries)

# def dfs(balance, cnt):
#     max_count = cnt  # 현재 방문한 나라 개수

#     for i in range(len(countries)):
#         if not check[i] and countries[i][0] <= balance:  # 비용이 balance 이하인 경우
#             check[i] = True
#             # 재귀 호출 후 반환된 최대 방문 수를 저장
#             max_count = max(max_count, dfs(balance - countries[i][0], cnt + 1))
#             check[i] = False  # 백트래킹

#     return max_count

print(dfs(balance, 0))
