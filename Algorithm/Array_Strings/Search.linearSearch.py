from array import array

arr =array('i',[38, 27, 43, 3, 9, 82, 10])

x = 10 
for i in arr:
    if i == x:
        print(f"Found {i} {x}")
        break
