arr =[3,4,5,6,8,4,3,2]

def second_largest(arr):
    if len(arr)<2:
        return None
    max_in = 0
    second_in = 0 
    for i in arr:
        if i >= max_in:
            max_in = i
    for i in arr : 
        if i >= second_in and i != max_in:
            second_in = i
    return second_in

def second_largest2(arr):
    if len(arr) < 2:
        return None  # Not enough elements to find the second largest
    first = second = float('-inf')
    for number in arr:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second

print(second_largest(arr))
print(second_largest2(arr))