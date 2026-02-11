from operator import le


arr2 = [1,2,3,4,5,6]
arr1= [3,4,6,9,10,72]


def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0 
    merge = []
    while i<len(arr1) and j < len(arr2): 
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i+=1
        else:
            merge.append(arr2[j])
            j+=1



    


merge_inserted_sorted_arrays(arr1, arr2)