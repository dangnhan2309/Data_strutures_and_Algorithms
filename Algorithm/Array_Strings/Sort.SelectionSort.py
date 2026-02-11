from array import array
import random
from tarfile import AREGTYPE
arr = array('i',[1,2,3,4,5,6,7,8,9,10])
arr_lis = list(arr)
random.shuffle(arr_lis)
array_num = array('i',arr_lis)

print("Unsorted array: ",array_num)

def selection_sort(arr):
	for i in range (len(arr)):
		min_index= i 
		for j in range(i,len(arr)):
			if arr[j]> arr[min_index]:
				arr[j],arr[min_index] = arr[min_index],arr[j]

	return arr
print("Sorted array: ",selection_sort(array_num))