nums = list(range(1, 50 + 1))
memo = [True] * len(nums)

memo[0] = False


def print_nums(memo, nums):
    for i in range(len(memo)):
        if memo[i]:
            print(nums[i], end=' ')
    print()


for j in range(2, 7 + 1):
    for i in range(j * 2 - 1, len(nums), j):
        memo[i] = False

print_nums(memo, nums)
