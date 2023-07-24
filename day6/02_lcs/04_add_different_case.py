str1 = "ABCDDBA"
str2 = "DCABDC"

dp = [[0] * (len(str1) + 1) for i in range(len(str2) + 1)]

for j in range(1, len(str2) + 1):
    for i in range(1, len(str1) + 1):
        if str2[j-1] == str1[i-1]:
            dp[j][i] = dp[j-1][i-1] + 1
        else:
            up = dp[j-1][i]
            left = dp[j][i-1]
            if up > left:
                dp[j][i] = up
            else:
                dp[j][i] = left

for row in dp:
    print(row)