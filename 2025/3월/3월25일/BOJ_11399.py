n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
result = 0
for i in range(1,len(numbers)): 
    numbers[i] = numbers[i-1] + numbers[i]
    
print(sum(numbers))