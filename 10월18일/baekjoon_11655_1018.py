n = input()
result = ""


for i in n : 
    if i.isalpha() and i.isupper() :
        n = (ord(i)-65+13)%26
        result = result+chr(n+65)

    elif i.isalpha() and i.islower() : 
         n = (ord(i)-97+13)%26
         result = result+chr(n+97)

    else :
        result = result+i     

print(result)