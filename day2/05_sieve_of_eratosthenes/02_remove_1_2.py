nums = list(range(1, 50 + 1))
memo = [True] * len(nums)

memo[0] = False

for i in range(3, len(nums), 2):
    print(nums[i], end=' ')
    memo[i] = False

print()
print(memo)
