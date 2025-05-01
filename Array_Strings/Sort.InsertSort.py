from array import array
from encodings.punycode import insertion_sort 
arr = array('i',[3,5,6,78,3,34,2,4])
def insertion_sort(arr): 
    for i in range(0,len(arr)): 
        key = arr[i]
        j = i -1 
        while j>= 0 and arr[j] > key: 
            arr[j+1 ]= arr[j]
            arr[j]= key 
            j -= 1
        arr[j+1] = key  
    return arr 
    
print(insertion_sort(arr))