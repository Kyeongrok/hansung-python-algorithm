
def permutations(nums, current_nums, result_set):
    print(current_nums)
    con = ''.join(current_nums)
    if con != '':
        result_set.add(int(con))

    if len(nums) == 0:
        return
    for n in nums:
        nums.remove(n)
        permutations(nums, current_nums + [n], result_set)
        nums.append(n)

s1 = set()
permutations(["0", "1", "1"], [], s1)
print(s1)