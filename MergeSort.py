
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

arr = [12, 11, 15, 50, 61, 72]  
print ("Given array is", end ="\n")  
for i in range(len(arr)):         
    print(arr[i], end =" ") 
print()  
mergeSort(arr) 
print("Sorted array is: ", end ="\n") 
for i in range(len(arr)):         
    print(arr[i], end =" ")
print()  
print("Analysis of Merge Sort - ->  Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation")
print("T(n) = 2T(n/2) + O(n) ")
print("And it gives the complexity of O(nLogn).Time complexity of Merge Sort is O(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and take linear time to merge two halves.")
