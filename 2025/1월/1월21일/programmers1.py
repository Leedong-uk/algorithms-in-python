from itertools import product
word = "AAAAE"
n = len(word)
alpha = ['A','E','I','O','U']
word_list=[]

for i in range(1,6) : 
    for j in list(product(alpha,repeat = i)):
        word_list.append(''.join(j))

word_list.sort()


    


