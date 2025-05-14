def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_arr
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Copy any remaining elements of right_arr
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# Test the function
arr_test = [2, 5, 6, 3, 7, 4, 3, 8, 1]
merge_sort(arr_test)
print(arr_test)



