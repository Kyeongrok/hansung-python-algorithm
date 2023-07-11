str1 = "ABCDDBA"
str2 = "DCABDC"

dp = [[0] * (len(str1) + 1) for i in range(len(str2) + 1)]

for j in range(1, len(str2) + 1):
    for i in range(1, len(str1) + 1):
        print(str2[j-1], str1[i-1])