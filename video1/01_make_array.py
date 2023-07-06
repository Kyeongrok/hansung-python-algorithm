from math import sqrt


def print_nums(memo, nums):
    for i in range(len(memo)):
        if memo[i]:
            print(nums[i], end=' ')
    print()

def primes(N):
    nums = list(range(1, N + 1))
    memo = [True] * len(nums) # is_prime
    memo[0] = False


    for j in range(1, int(sqrt(N))):
        if memo[j]:
            # print(nums[j])
            for i in range(nums[j] * 2 - 1, len(nums), nums[j]):
                memo[i] = False

    print_nums(memo, nums)

primes(500)



