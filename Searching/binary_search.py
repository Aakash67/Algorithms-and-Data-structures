#Binary Search in python
def binary_search(lis,target):
    low=0
    high=len(lis)-1
    # Repeat until the pointers low and high meet each other
    while low<=high:
        #Find the middle element of list
        mid=(low+high)//2
        if lis[mid]==target:
            return mid
        elif lis[mid]<target:
            low=mid+1
        else:
            high=mid-1
    else:
        return -1
            
#The List must be in sorted order for the Binary Search
lis=[2,4,6,8,14,18,20]
target=int(input("Enter the target element"))
result=binary_search(lis,target)
if(result==-1):
    print("The Target element is not found at the list")
else:
    print("The Target element is found at the index of",result)