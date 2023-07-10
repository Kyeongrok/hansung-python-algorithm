def sum(arr):
    print(arr)
    if len(arr) == 0:
        return 0
    return arr.pop() + sum(arr)

arr = [7, 3, 2, 9]
print(sum(arr))

