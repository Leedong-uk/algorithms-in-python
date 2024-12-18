a = 5  # 5월
b = 24  # 24일
day = {0: "SUN", 1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT"}
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

current_yoil = 5  # 2016년 1월 1일 금요일(FRI)

for i in range(a-1):  
    for _ in range(month[i]) : 
        current_yoil = (current_yoil + 1) % 7

for _ in range (b-1) :
    current_yoil = (current_yoil + 1) % 7
    
# 최종 요일 출력
print(day[current_yoil])
