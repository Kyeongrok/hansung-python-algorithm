arr = [7, 2, 3, 9, 28, 1]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        # print(i, j, j - 1)
        print(arr[i], arr[j], arr[j - 1])
        if arr[j] < arr[j - 1]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
        else:
            break
    print(arr)
