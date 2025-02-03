from datetime import date,timedelta 
a = 5
b = 24
start_date = date(2016,1,1)
end_date = date(2016,a,b)
yoil = {0:'SUN',1:'MON',2:'TUE',3:'WED',4:'THU',5:'FRI',6:'SAT'}
start_yoil = 5
while start_date < end_date  : 
    start_date += timedelta(days = 1)
    start_yoil = (start_yoil +1)%7

print(yoil[start_yoil])