arr = [12,3,45,32,65,99,76,33]
large_element = arr[0]
for i in range(len(arr)):
    if (arr[i]>large_element):
        large_element = arr[i]
    
print(f"large element is {large_element}")