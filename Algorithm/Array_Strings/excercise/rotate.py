arr= [1,2,4,5,7,3,3,5,3,6,8]

def rotate_left(arr,k): 
    return arr[k:] + arr[:k]
def rotate_right(arr,k): 
    return arr[-k:] + arr[:-k]
print(arr)
print(rotate_left(arr,2))
print(arr)
print(rotate_right(arr,2))