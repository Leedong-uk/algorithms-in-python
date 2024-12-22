from datetime import date

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
terms_dict = {}
answer=[]

today_year,today_month,today_day = map(int,today.split("."))
today_date = date(today_year,today_month,today_day)

for i in terms : 
    key,value = i.split()
    terms_dict[key] = int(value)


for i in range(len(privacies)) : 
    privacies_date , key = privacies[i].split()
    year,month,day = map(int, privacies_date.split("."))
    update = month + terms_dict[key]
    
    new_year = year + update // 12 
    
    new_month =update %12
    if new_month == 0 :
        new_year -=1
        new_month = 12

    new_day = day-1
    if new_day == 0 :
        new_month -=1
        new_day = 28
        if new_month == 0 :
            new_year -=1
            new_month = 12

    new_date = date(new_year,new_month,new_day)

    if new_date < today_date : 
        answer.append(i+1)
print(answer)
    
    
    
