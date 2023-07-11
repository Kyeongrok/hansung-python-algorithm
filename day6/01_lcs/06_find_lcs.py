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


i = len(str1)
j = len(str2)
lcs = ""

print(dp[j][i])
while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]: # 같으면 대각선
        lcs = str1[i-1] + lcs
        i -= 1
        j -= 1
    elif dp[j-1][i] >= dp[j][i-1]: # 위가 크거나 같으면 위로
        j -= 1
    else:
        i -= 1

print(lcs)