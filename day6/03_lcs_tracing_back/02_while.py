from lcs import make_dp

str1 = "ABCDDBA"
str2 = "DCABDC"
dp = make_dp(str1, str2)

for row in dp:
    print(row)

j = len(str1)
i = len(str2)
lcs = ""

while j > 0 and i > 0:
    if str1[j - 1] == str2[i - 1]:
        lcs = str1[j - 1] + lcs
        i -= 1
        j -= 1
    elif dp[i][j - 1] > dp[i - 1][j]:
        j -= 1
    else:
        i -= 1

print(lcs)