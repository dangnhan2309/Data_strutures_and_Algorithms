def split_even_odd(arr):
    even = []
    odd = []
    for num in arr: 
        if num % 2 == 0 : 
            even.append(num)
        else:
            odd.append(num)
    return even + odd

def split_even_odd2(arr):
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 != 0]
    return even + odd
def split_even_odd3(arr):
    index = 0  # Index to track the placement of swapped elements
    
    # If the first element is even, move all odd numbers behind
    if arr[0] % 2 == 0:
        for i in range(len(arr)):
            if arr[i] % 2 != 0:  # Found an odd number
                arr[index], arr[i] = arr[i], arr[index]  # Swap
                index += 1  # Move the index forward
    else:
        # If the first element is odd, move all even numbers behind
        for i in range(len(arr)):
            if arr[i] % 2 == 0:  # Found an even number
                arr[index], arr[i] = arr[i], arr[index]  # Swap
                index += 1  # Move the index forward
                
    return arr

# Example usage
arr = [3, 1, 2, 4, 5, 6, 7, 8]
print(split_even_odd3(arr))  # Output will have evens first or odds first based on arr[0]
