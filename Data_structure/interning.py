a = 256
b = 256
print(a is b)  # True (Cùng trỏ về một vùng nhớ - Alias)

x = 257
y = 257
print(x is y)  # False (Với số lớn hơn, Python tạo 2 đối tượng riêng biệt)