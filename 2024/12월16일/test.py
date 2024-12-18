s=input()
number = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
number_key = list(number.keys())
result = []
temp =''
for i in s : 
    if i.isdigit() : 
        result.append(int(i))
    else : 
        temp +=i
        if temp in number_key : 
            result.append(number[temp])
            temp = ''

for i in result : 
    print(i,end='')


