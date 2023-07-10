def sort(arr):
    if len(arr) == 0:
        return []
    pivot = 0
    pivot_value = arr[pivot]

    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot_value:
            left.append(arr[i])
        elif arr[i] > pivot_value:
            right.append(arr[i])

    return sort(left) + [pivot_value] + sort(right)

arr = [7, 2, 3, 9, 28, 1]
print(sort(arr))
