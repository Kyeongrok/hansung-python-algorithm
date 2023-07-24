from lcs import make_dp

str1 = "ABCDDBA"
str2 = "DCABDC"
dp = make_dp(str1, str2)

for row in dp:
    print(row)

j = len(str2)
i = len(str1)

print(j, i)