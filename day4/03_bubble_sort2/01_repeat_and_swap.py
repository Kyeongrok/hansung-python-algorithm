arr = [7, 2, 3, 9, 28, 1]

j = 0
for i in range(1, len(arr)):
    if arr[j] > arr[i]:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
    print(arr)
