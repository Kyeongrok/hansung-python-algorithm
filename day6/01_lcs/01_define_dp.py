
str1 = "ABCDDBA"
str2 = "DCABDC"

row = [0] * (len(str1) + 1)
dp = [row] * len(str2)

dp[1][2] = 1

for row in dp:
    print(row)