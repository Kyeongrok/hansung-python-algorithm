nums = list(range(1, 50 + 1))
memo = [True] * len(nums)

memo[0] = False


def print_nums(memo, nums):
    for i in range(len(memo)):
        if memo[i]:
            print(nums[i], end=' ')
    print()


for j in range(1, 7):
    if memo[j]:
        for i in range(nums[j] * 2 - 1, len(nums), nums[j]):
            memo[i] = False
        print(nums[j], memo[j])

print_nums(memo, nums)
