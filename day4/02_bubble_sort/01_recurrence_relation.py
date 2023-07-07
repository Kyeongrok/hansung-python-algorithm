arr = [7, 2, 3, 9, 28, 11]

temp = arr[0]
arr[0] = arr[1]
arr[1] = temp
print(arr)

temp = arr[1]
arr[1] = arr[2]
arr[2] = temp
print(arr)