can = ["aya", "ye", "woo", "ma" ]
cant_s = ['ayaaya','yeye','woowoo','mama']
babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
#ayeya
for word in babbling : 
    for i in cant : 
        if i in word : 
            word = word.replace(i,'x')
    
    for i in can : 
        if i in word : 
            word = word.replace(i.' ')
    
    word = word.replace(' '.'')

    if word == '' :
        answer +=1
