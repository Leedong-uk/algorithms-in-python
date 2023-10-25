#이 문제를 틀린이유
#왜이렇게 어렵게 생각하는지 모르겠다
#dp 테이블을 작성할떄 앞에서 순차적으로 하나하나 쌓아가야한다
#그렇게 쌓아가면서 규칙을 찾아야한다 또 dp 테이블의 정의를 잘 생각해야한다
#i번쨰에서 연속합의 최대값 즉 i번쨰의 숫자를 선택을하면 이전 값에서 더해주면 되는거고
#숫자를 선택하지않으면 더이상 연속이 되지 않음으로 0을 기입을 해야한다 

N = int(input())
lst = [0]+list(map(int,input().split()))

dp = [0]*(N+1)

if max(lst[1:])<0:
    ans = max(lst[1:])

else : 
    for i in range(1,N+1):
        dp[i] = max(0,dp[i-1]+lst[i])
    
    ans = max(dp)

print(ans)
