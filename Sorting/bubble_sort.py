# Bubble Sort in python
def bubble(lis):
    for i in range(len(lis)):
        for j in range(0,len(lis)-1):
            #for desending order change lis[j]<lis[j+1] to lis[j]>lis[j+1]
            if lis[j]<lis[j+1]:
                temp=lis[j]
                lis[j]=lis[j+1]
                lis[j+1]=temp
    
lis=[2,4,3,1,6,7]
bubble(lis)
print("The List is sorted using bubble sort",lis)