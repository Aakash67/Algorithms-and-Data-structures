def linearsearch(lis,target):
    for i in range(len(lis)):
        if lis[i]==target:
            return i
    else:
        return -1
    
lis=[1,2,3,4,5,6,7,8,9,10]
target=int(input("Enter the element to be found"))
result=linearsearch(lis,target)
if (result==-1):
    print("The Target element is not found in the list")
else:
    print("The Target element is found in the index ",result)