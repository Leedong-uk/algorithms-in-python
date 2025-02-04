from datetime import date 
today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
result = []
dic = {}

today_year,today_month,today_day = map(int,today.split("."))
today_date = date(today_year,today_month,today_day)

for i in terms : 
    key,value = i.split()
    dic[key] = int(value)

for i in range(len(privacies)) : 
    day , key = privacies[i].split()
    year,month,day = map(int,day.split("."))
    
    day += 28*dic[key]
    update_month = day//28
    day = day%28

    if day == 0 : 
        day = 28
    

    month +=update_month
    update_year = month//12
    month = month%12

    if month == 0 :
        month = 12

    year +=update_year

    print(year,'.',month,'.',day)
    print('----------------------------')
    deadline = date(year,month,day)

    if today_date >=deadline : 
        result.append(i+1)

print(result)


