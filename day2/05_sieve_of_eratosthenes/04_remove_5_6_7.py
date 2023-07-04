nums = list(range(1, 50 + 1))
memo = [True] * len(nums)

memo[0] = False

print(nums)

def print_nums(memo, nums):
    for i in range(len(memo)):
        if memo[i]:
            print(nums[i], end=' ')
    print()


for i in range(3, len(nums), 2):
    memo[i] = False
print_nums(memo, nums)

for i in range(5, len(nums), 3):
    memo[i] = False
print_nums(memo, nums)

for i in range(7, len(nums), 4):
    memo[i] = False
print_nums(memo, nums)

# 5
for i in range(9, len(nums), 5):
    memo[i] = False
print_nums(memo, nums)

# 6
for i in range(11, len(nums), 6):
    memo[i] = False
print_nums(memo, nums)

# 7
for i in range(13, len(nums), 7):
    memo[i] = False
print_nums(memo, nums)
