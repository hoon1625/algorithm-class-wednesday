n = int(input("계단의 개수를 입력하시오: "))

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = 1
if n >= 2:
    dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(f"{n}개의 계단을 오르는 방법의 수는 {dp[n]}가지입니다.")