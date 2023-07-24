
def permutation(nums, current_nums, result):
    print(current_nums)
    result.append(current_nums)

    for num in nums:
        if num not in current_nums:
            permutation(nums, current_nums + [num], result)


result = []
permutation([1, 2, 3], [], result)

print(result)