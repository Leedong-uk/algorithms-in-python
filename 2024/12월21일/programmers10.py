def solution(new_id):
    result = ''
    check='abcdefghijklmnopqrstuvwxyz0123456789-_.'

    #1번
    new_id = new_id.lower()

    #2번 (틀)
    new_id = ''.join([i for i in new_id if i in check])

    #3번 (틀)
    while '..' in new_id : 
        new_id = new_id.replace('..',".")
    #4번
    if len(new_id) >0 and new_id[0] =='.' :
        new_id = new_id[1:]
    if len(new_id) >0 and new_id[-1] =='.' : 
        new_id = new_id[:-1]

    #5번
    if len(new_id) == 0 :
        new_id = 'a'
    #6번
    if len(new_id) >=16 : 
        new_id = new_id[:15]
        if new_id[-1] == '.' : 
            new_id = new_id[:-1]
    #7번 (틀)
    while len(new_id) <3 :
        new_id += new_id[-1]
        
    return new_id