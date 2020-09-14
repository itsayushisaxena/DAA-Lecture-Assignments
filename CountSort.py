def count_sort(arr): 
    max_element = int(max(arr)) 
    min_element = int(min(arr)) 
    element_range = max_element - min_element + 1
    count_arr = [0 for _ in range(element_range)] 
    out_arr = [0 for _ in range(len(arr))] 

    for i in range(0, len(arr)): 
        count_arr[arr[i]-min_element] += 1

    for i in range(1, len(count_arr)): 
        count_arr[i] += count_arr[i-1] 

    for i in range(len(arr)-1, -1, -1): 
        out_arr[count_arr[arr[i] - min_element] - 1] = arr[i] 
        count_arr[arr[i] - min_element] -= 1

    for i in range(0, len(arr)): 
        arr[i] = out_arr[i] 
    return arr 

arr = [15, 10, 0, 3, 8, 5, 1, 16] 
ans = count_sort(arr) 

print("Sorted character array is " + str(ans))
print(" Analysis of Count Sort --->  Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Its time complexity is O(n+k) where n is the number of elements in input array and k is the range of input. ")
