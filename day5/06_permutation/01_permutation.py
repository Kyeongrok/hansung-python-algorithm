def permutation(nums, current_nums):
    print(current_nums)

    for num in nums:
        if num not in current_nums:
            permutation(nums, current_nums + [num])


permutation([1, 2, 3], [])

