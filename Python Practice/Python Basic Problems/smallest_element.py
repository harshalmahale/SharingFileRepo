arr = [10,89,12,9,7,14,21,1,15,98]
mini = arr[0]

for i in range(len(arr)):
    if arr[i]<mini:
        mini = arr[i]

print(mini)