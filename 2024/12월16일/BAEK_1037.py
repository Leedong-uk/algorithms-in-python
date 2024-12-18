n = int(input())
number = list(map(int, input().split()))
number.sort()

if n == 1:
    print(number[0] ** 2)
else:
    print(number[0] * number[-1])
