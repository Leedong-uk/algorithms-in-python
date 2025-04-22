new_id = "...!@BaT#*..y.abcdefghijklm"
check='abcdefghijklmnopqrstuvwxyz0123456789-_.'
print("원본:",new_id)

# 1단계
new_id = new_id.lower()
print("1단계:",new_id)

# 2단계
new_id = ''.join([i for i in new_id if i in check])
print("2단계 : ",new_id)

# 3단계
while ".." in new_id :
    new_id = new_id.replace("..",".")
print("3단계 : ",new_id)

# 4단계
if new_id[0] == "." : 
    new_id = new_id[1:]
elif new_id[-1] =="." :
    new_id = new_id[:-1]
print("4단계 : ",new_id)

# 5단계
if  not new_id : 
    new_id = "a"
print("5단계 : ",new_id)

# 6단계
if len(new_id) >=16 : 
    new_id = new_id[:15]
    if new_id[-1] =="." :
        new_id = new_id[:-1]
print("6단계 : ",new_id)

# 7단계
while len(new_id) <3 :
    new_id += new_id[-1]
print("7단계 : ",new_id)