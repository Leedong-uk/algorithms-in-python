"""""
#2진수를 8진수로 바꾸는방법 ->3자리씩 끊어서 8진수로 변환하면된다 
import sys
N = sys.stdin.readline().rstrip()[::-1]
ans = ''
tmp = 0		# 각 자릿수의 계산 결과를 담을 변수
cnt = 1		# 곱해줄 배수 : 1,2,4

for i in N:
    if(cnt < 8):
        tmp += cnt * int(i)
        cnt *= 2	
    else:
        ans += str(tmp)
        tmp = 1 * int(i)
        cnt = 2
ans += str(tmp)
print(int(ans[::-1])) 
"""
#시간초과뜸 
#인터넷 검색해보니 내장 함수가 있었음
#내장함수 기피하지말고 사용하자 ->너의 무기가 됨
print(oct(int(input(),2))[2:])
#먼저 input(),2 -> input()뒤에 , (숫자) 하면 해당 숫자진수로 바꿔줌 여기선 2가 들어왔음으로 2진수로 입력받는거야
#그다음 입력받은 2진수를 10진수로 바꿔줬음 단순히 int만씌우면됨(int(input(),2))
#마지막으로 10진수를 8진수로 바꿔줌 oct(10진수 정수) ->oct(int(input(),2))
#정리) 2진수입력받고->10진수변환->8진수 출력