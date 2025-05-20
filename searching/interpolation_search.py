def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Calculate position using interpolation formula
        pos = low + int(((high - low) / (arr[high] - arr[low])) * (target - arr[low]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Use a sorted array for interpolation search
print(interpolation_search(sorted([1,2,3,4,5,6,7,18,9,12]), 18))
       
        
        
                 
        
        