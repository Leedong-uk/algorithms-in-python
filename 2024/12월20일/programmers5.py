keymap = ["ABACD", "BCEFD"]
targets =["ABCD","AABB"]
answer=[]



for target_word in targets : 
    result = 0
    for target_word_letter in target_word :
        min_number = 101
        for keymap_word in keymap : 
            number = keymap_word.find(target_word_letter)
            if number != -1 : 
                min_number =min(min_number,number+1)
            
        if min_number == 101 :
            result =-1
        else :
            result += min_number
    answer.append(result)

print(answer)