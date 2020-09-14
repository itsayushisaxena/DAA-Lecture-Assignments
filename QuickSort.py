def quicksort(arr,low,high):


    if low<high:
    

       pi=partition(arr,low,high) 

       quicksort(arr,low,pi-1)
   

       quicksort(arr,pi+1,high)



def partition(arr,low,high):


    p=arr[low]


    i=low

    j=i+1


    while(j<=high):
    

        if(arr[j]<=p):

            i+=1


            arr[i],arr[j]=arr[j],arr[i]

        j+=1


    arr[i],arr[low]=arr[low],arr[i]
  

    return i

 

arr = [10,15,8,6,20,1]


n=len(arr)


quicksort(arr,0,n-1)

print("sorted array:")


for i in range(n):


    print("%d" %arr[i])
print("Analysis of quick sort -  -> Time taken by QuickSort in general is ")
print("          T(n) = T(k) + T(n-k-1) + (n)             ")
print("The time taken by QuickSort depends upon the input array and partition strategy.The worst case occurs when the partition process always picks greatest or smallest element as pivot.The worst case would occur when the array is already sorted in increasing or decreasing order and the complexity will be O(n).The best case occurs when the partition process always picks the middle element as pivot and gives the complexity O(nLogn).For Average case analysis, we need to consider all possible permutation of array and calculate time taken by every permutation.")

