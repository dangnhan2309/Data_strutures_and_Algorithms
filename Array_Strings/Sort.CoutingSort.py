def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Bước 1: Đếm số lượng
    for num in arr:
        count[num] += 1
#arr = [4, 2, 2, 8, 3, 3, 1]
#count = [0,1,2,2,1,0,0,0,1]

    # Bước 2: Cộng dồn
    print("count: truoc") 
    print(count) 
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    print("count: sau") 
    print(count) 
    #i =1 -> count[1] = 0 + 1 = 1
#arr = [4, 2, 2, 8, 3, 3, 1]
#count = [0,1,3,5,6,1,6,6,7]



    # Bước 3: Sắp xếp vào mảng output
    output = [0] * len(arr)
    for num in reversed(arr):  # Duyệt từ phải qua trái để ổn định
        output[count[num] - 1] = num
        count[num] -= 1
#arr = [4, 2, 2, 8, 3, 3, 1]
#       0  1  2  3  4  5  6  7  8
# num = 1 -> count[1] -1  = 0 -> output [0]= 1 , -> out = [1,]
#count = [0,0,3,5,6,1,6,6,7]
# num = 3 -> count[3] =5-1  = 4 -> output [4]= 3 , -> out = [1,0,0,0,3,0,0,0]
#count = [0,0,3,4,6,1,6,6,7]
# num = 3 -> count[3] =4-1  = 3 -> output [3]= 3 , -> out = [1,0,0,3,3,0,0]
#count = [0,0,3,3,6,1,6,6,7]
# num = 8 -> count[8] =7-1  = 6 -> output [6]= 8 , -> out = [1,0,0,3,3,0,8]
#count = [0,0,3,3,6,1,6,6,6]
# num = 2 -> count[2] =3-1  = 2 -> output [2]= 2 , -> out = [1,0,2,3,3,0,8]
#count = [0,0,2,3,6,1,6,6,6]
# num = 2 -> count[2] =2-1  = 1 -> output [1]= 2 , -> out = [1,2,2,3,3,0,8]
#count = [0,0,1,3,6,1,6,6,6]
# num = 4 -> count[4] =6-1  = 5 -> output [5]= 4 , -> out = [1,2,2,3,3,4,8]
    return output
arr = [4, 2, 2, 8, 3, 3, 1]
result = counting_sort(arr)
print("Sorted array:", result)