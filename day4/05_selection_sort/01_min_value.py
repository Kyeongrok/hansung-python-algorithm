arr = [7, 2, 3, 9, 28, 11]

for i in range(len(arr)):
    target_value = arr[i]
    target_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < target_value:
            target_value = arr[j]
            target_idx = j
    print(target_value, target_idx)
