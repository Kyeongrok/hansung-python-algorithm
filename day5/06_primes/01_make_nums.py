
def combination(nums, current_nums):
    print(current_nums)
    for i in range(len(nums)):
        if len(current_nums) < 3:
            combination(nums.pop(), current_nums + nums.pop())

combination(["0", "1", "1"], [])