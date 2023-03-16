#Insertion sort using python in both Ascending and Descending order
def insertion(lis):
    for i in range(1,len(lis)):
        key=lis[i]
        j=i-1
        #for descending order change key<lis[j] to key>lis[j]
        while j>=0 and key<lis[j]:
            lis[j+1]=lis[j]
            j=j-1
        lis[j+1]=key
                
    
lis=[10,1,3,7,5,9,2,4]
insertion(lis)
print("The Sorted list is",lis)
