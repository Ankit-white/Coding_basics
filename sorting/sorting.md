Bubble sort : it is a sorting technique in which we will using a third variable and swaping the numbers within the loop 
in this method we have several itreation in 1 itreation we will find out the largest number,
in second itreation last second highest and  it will goo on upto the array is sorted

def bubblesort(list):
    for i in range(len(list)-1,0,-1): # i will run from right to left
        for j in range(i):
            if list[j]>list[j+1]: # it checks the number if the number is greater than it will swap
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list   # it will return the value 

print(bubblesort([2,3,5,1,4,8,7]))  



Insertion sort : it is a sorting technique in which it will swap the number without using third variable 
deff between bubble sort and this is it will go from right to left but in bubble sort it will go from left to right 



def insertionsort(arr):
    for i in range(1,len(arr)): # i value will be commiting from right to left i.e 1 to lentgh of array
        j=i
        while arr[j-1]>arr[j] and j > 0: # it will check for 2 conditions arr[j-1]> arr[j] and j> 0 if both are true it will run the loop statements
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j -= 1
    return arr        
print(insertionsort([2,3,5,4,6,8,7]))



Merge sort: it is a sorting method technique in which it just divide and conquer the arr i.e it split the arr in half or it will divide to upto we get simplest form to solve and recursion takes place of merge sort and it will merge the two hals into a sorted arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # from this we get mid number for spliting
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr) # in this we recursive the merge sort i.e recall the function within the function

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









