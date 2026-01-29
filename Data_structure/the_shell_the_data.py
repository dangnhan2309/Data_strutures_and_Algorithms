import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)

# 1. Kích thước của "khung" đối tượng
shell_size = sys.getsizeof(p) 
print(f"{shell_size} day la shell size")
# 2. Kích thước của dictionary chứa x và y
attr_size = sys.getsizeof(p.__dict__)
print(f"{attr_size} day la attributes size")

total = shell_size + attr_size
print(f"Tổng dung lượng: {total} bytes")