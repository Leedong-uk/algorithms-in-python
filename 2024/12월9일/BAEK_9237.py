n = int(input())
 
day = list(map(int, input().split()))
day.sort(reverse=True)
 
for i in range(len(day)):
    day[i] = day[i] + (i + 1)	# 묘목을 심는데 걸리는 일수(누적) + 1일부터 시작
 
print(max(day)+1)