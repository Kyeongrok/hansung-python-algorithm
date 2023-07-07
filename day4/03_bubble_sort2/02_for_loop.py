arr = [7, 2, 3, 9, 28, 1]

for j in range(len(arr) - 1):
    for i in range(1 + j, len(arr)):
        if arr[j] > arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
        print(j, arr)