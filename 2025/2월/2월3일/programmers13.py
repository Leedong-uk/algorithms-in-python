#코드번호,제조일,최대수량.현재수량
#정렬기준 : ext
#정렬기준 값 : val_ext
#정보를 정렬할 기준이 되는 문자열 : sort_by
#ext값이 val_ext 보다 작은 데이터만 뽑은후 sort_by로 오름차순 정렬
result = []
data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext_dic = {'code':0,'date':1,'maximum':2,'remain':3}

ext = "date"
val_ext = 20300501
sort_by = "remain"

for i in data : 
    if i[ext_dic[ext]] < val_ext : 
        result.append(i)

result.sort(key = lambda x : x[ext_dic[sort_by]])
print(result)
