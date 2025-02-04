result = ''
check='abcdefghijklmnopqrstuvwxyz0123456789-_.'
new_id ="...!@BaT#*..y.abcdefghijklm"

new_id = new_id.lower()
new_id = ''.join([i for i in new_id if i in check])

while '..' in new_id : 
    new_id = new_id.replace("..",".")

if len(new_id) >0 and new_id[0] =='.' :
    new_id = new_id[1:]
if len(new_id) >0 and new_id[-1] =='.' : 
    new_id = new_id[:-1]

if not new_id : 
    new_id = 'a'

if len(new_id)>=16 : 
    new_id = new_id[:15]
    if new_id[-1] == '.' : 
        new_id = new_id[:-1]

while len(new_id) <3 : 
    new_id += new_id[-1]
    
