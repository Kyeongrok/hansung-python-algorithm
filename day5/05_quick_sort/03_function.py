def sort(arr):
    pivot = 0
    pivot_value = arr[pivot]

    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot_value:
            left.append(arr[i])
        elif arr[i] > pivot_value:
            right.append(arr[i])

    return left + [pivot_value] + right

arr = [7, 2, 3, 9, 28, 1]
print(sort(arr))
