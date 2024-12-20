s = "aukks"
skip = "wbqd"
index = 5
result = ''
for i in s : 
    x = ord(i)
    while index !=0 : 
        x = 97 + (((x-97)+1)%26)
        if chr(x) not in skip : 
            index -=1
    
    result +=chr(x)
    index = 5

print(result)