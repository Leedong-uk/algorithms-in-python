
# dp너무 어렵다 복습해보기!dp너무 어렵다 복습해보기!dp너무 어렵다 복습해보기!dp너무 어렵다 복습해보기!dp너무 어렵다 복습해보기!dp너무 어렵다 복습해보기!
# 내가 할수 있겠지... ㅜㅜㅜㅜ
import sys

x= int(sys.stdin.readline().rstrip())
dp = [[0]*12 for _ in range(x+1)]

dp[1][2:11] = [1]*9

for i in range(2,x+1) : 
    for j in range(1,11):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]


ans = sum(dp[x])
print(ans%1000000000)