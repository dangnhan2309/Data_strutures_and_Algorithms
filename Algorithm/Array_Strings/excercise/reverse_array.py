from array import array

arr = array('i',[1,2,3,4,5,6,7])
arr_v = arr[::-1]
arr_v2 = reversed(arr)

print(arr[1])
print(arr_v)
print(list(arr_v2))