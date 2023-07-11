str1 = "ABCDDBA"
str2 = "DCABDC"

dp = [[0] * (len(str1) + 1) for i in range(len(str2) + 1)]

dp[1][2] = 1

for row in dp:
    print(row)