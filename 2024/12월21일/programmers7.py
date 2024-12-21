#code / date / maximum / remain
data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"
ext_dic = {'code':0,'date':1,'maximum':2,'remain':3}
result=[]

for i in data : 
    if i[ext_dic[ext]] < val_ext : 
        result.append(i)

result.sort(key = lambda x : x[ext_dic[sort_by]])
print(result)
