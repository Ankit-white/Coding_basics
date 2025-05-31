def find_maximum(arr, length):
    max_val = arr[0]
    for j in range(length):
        if arr[j] > max_val:
            max_val = arr[j]
    return max_val

def find_minimum(arr, length):
    min_val = arr[0]
    for i in range(length):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val        

# Input section
n = 7
arr = [1,2,3,4,5,7,8]


# Output
print(find_minimum(arr, n))
print(find_maximum(arr, n))



    