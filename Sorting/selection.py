#Selection sort using python
def selection(lis):
    for i in range(0,len(lis)):
        min_index= i
        for j in range(i+1,len(lis)):
            #for decsending order change lis[j]<lis[min_index] to lis[j]>lis[min_index]
            if lis[j]<lis[min_index]:
                min_index = j
            #swaping the minimum value
        lis[i],lis[min_index]=lis[min_index],lis[i]
            

lis=[7,5,4,3,2,8,1]
selection(lis)
print("The List is sorted using selection sort",lis)