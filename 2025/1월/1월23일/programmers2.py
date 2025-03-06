prices = [1, 2, 3, 2, 3]
answer = [0] * len(prices)
stack = []  # 스택에는 인덱스를 저장

for i in range(len(prices)):
    # 현재 가격이 스택의 마지막 가격보다 작으면
    while stack and prices[i] < prices[stack[-1]]:
        idx = stack.pop()  # 떨어진 가격의 인덱스
        answer[idx] = i - idx  # 유지 시간 계산
    
    stack.append(i)  # 현재 인덱스를 스택에 추가

# 스택에 남아 있는 인덱스 처리 (끝까지 가격이 떨어지지 않은 경우)
while stack:
    idx = stack.pop()
    answer[idx] = len(prices) - idx - 1

print(answer)
