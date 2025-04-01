n = int(input())
numbers = []
total = 0
for _ in range(n) : 
    x,y = map(int,input().split())
    numbers.append((x,y))
    total +=y

median = total / 2
temp = 0 

numbers.sort()
for x,y in numbers : 
    temp += y
    
    if temp >= median  : 
        
        print(x)
        break

# n = int(input())  
# numbers = []  
# total = 0  

# for _ in range(n):
#     x, a = map(int, input().split())
#     numbers.append((x, a))  
#     total += a  

# numbers.sort()


# median = total / 2
# temp = 0  

# for x, a in numbers:
#     temp += a  
#     if temp >= median:  
#         print(x)
#         break
