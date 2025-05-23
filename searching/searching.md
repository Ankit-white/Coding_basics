Binary search : it is a searching method in which it will frst go for the frst number last number and middle number.
if targert number is the middle number than it returns the value , if target numbar is greater than mid number than frst number will be middle number + 1 ,if the target is smaller than high value will be middle value - 1.it will run the loop when the target value matched it will jumps out of loop

def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high=mid-1
    return -1        
arr=[1,2,3,4,5,6,7,8,9,0,12,13,14,15]

print(binarysearch(arr,1))      





febonacci series: 
