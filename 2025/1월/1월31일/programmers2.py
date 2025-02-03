'''def solution(numbers):
    answer = []
    
    for num in numbers:
        next_num = num + 1  # num보다 큰 수부터 시작
        while True:
            # num과 next_num의 비트 차이를 계산
            if bin(num ^ next_num).count('1') <= 2:
                answer.append(next_num)
                break
            next_num += 1  # 차이가 2개를 초과하면, 다음 수로 넘어가서 다시 체크
    
    return answer
'''
def solution(numbers):
    return [((num ^ (num+1)) >> 2) + num + 1 for num in numbers]

# num보다 큰 수 중에서 num 의 2진수 와 비트수가 2개 이하로 차이나는 최소의 수를 구하는것
# 1. XOR 연산을 통해 비트수가 얼마나 그리고 어디서 차이나는지 확인
# 2. 시프트 2 연산을 통해 서로 다른 점 이 2개 이하를 구현
     #(만약 서로 다른 지점이 1개라면 RIGHT Shift 1 칸 해줌 )