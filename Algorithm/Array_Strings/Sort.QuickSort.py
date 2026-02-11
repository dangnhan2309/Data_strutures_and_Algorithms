from array import array

arr = array('i',[3,5,6,78,3,34,2,4])


def quicksort(arr):
	if len(arr) <=1:
		return arr
	else:
		pivot = arr[-1]
		left = [x for x in arr[:-1] if x <= pivot]
		right = [x for x in arr[:-1] if x > pivot]
	return quicksort(left) + [pivot] + quicksort(right)
print(quicksort(arr))


arr2 = array('i',[3,5,6,78,3,34,2,4])

def partition(arr,low,hight):
	pivot = arr[hight]
	i = low -1
	for j in range(low,hight):
		if arr[j] > pivot :
			i += 1
			arr[i],arr[j] = arr[j],arr[i]
	arr[i+1],arr[hight] = arr[hight],arr[i+1]	
	return i + 1	
def quick_sort(arr,low,hight):
	if low < hight:
		pi = partition(arr,low,hight)
		quick_sort(arr,low,pi-1)
		quick_sort(arr,pi+1,hight)
quick_sort(arr2,0,len(arr2)-1)
print(arr2)

