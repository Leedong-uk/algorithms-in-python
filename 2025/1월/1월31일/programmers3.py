'''
------------------------------------------------------------------
*compare(a, b) 반환값의 의미*
 compare(a, b)가   음수 (-1) → a가 b보다 앞에 와야 함
 compare(a, b)가   양수 (1)  → b가 a보다 앞에 와야 함
 compare(a, b)가     0       → 순서를 변경하지 않음
--------------------------------------------------------------------------------------
'''


from functools import cmp_to_key

# 비교 함수
def compare(a, b):
    if a + b > b + a:
        return -1  # a가 먼저 와야 함
    elif a + b < b + a:
        return 1   # b가 먼저 와야 함
    return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    # 결과가 "0"만 있는 경우는 "0"을 반환
    if numbers[0] == "0":
        return "0"

    return ''.join(numbers)

# 예시
print(solution([6, 10, 2]))  # "6210"
print(solution([3, 30, 34, 5, 9]))  # "9534330"
