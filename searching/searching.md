Binary search : it is a searching method in which it will frst go for the frst number last number and middle number.
if targert number is the middle number than it returns the value , if target numbar is greater than mid number than frst number will be middle number + 1 ,if the target is smaller than high value will be middle value - 1.it will run the loop when the target value matched it will jumps out of loop

def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2 #it will calculate the mid value by mean method
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high=mid-1
    return -1        
arr=[1,2,3,4,5,6,7,8,9,0,12,13,14,15]

print(binarysearch(arr,1))      





febonacci series: it is a sequence of number in which the number is sum of previous two numbers 




def fabonacci (n):
    feb = [0,1]
    x = 0
    for i in range (1,n):
        x = feb[i] + feb[i-1]  #x is the the number we get when the previous two numbers are added
        feb.append(x) # feb variable is added the numbers of x in the list
    return feb
        
print(fabonacci (10) )



Interpolation search: it is kind of searching which is similar to the binary search where will find the pos value by a formula 
pos = low + int(((high - low) - (arr[high]-arr[low])) * (target-arr[low]))

from this we will find middle position and we will run the the loop with a if statment if arr[pos]==target we will return pos 
else we will change the low and high value with pos +1,pos - 1 .


Linear search: it is a simple searching technique in which it will go in range of len of given array it will change the i value according to the range if the arr[i] == target it will return the i value i not loops contiue till the i will get the tareget positon
