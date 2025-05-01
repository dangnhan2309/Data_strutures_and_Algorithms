from array import array

arr = array('i',[3,5,6,78,3,34,2,4])

def bubble_sort(arr):
    for i in range(len(arr)): 
        for j in range(i,len(arr)):
            if arr[i]> arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
print(bubble_sort(arr))