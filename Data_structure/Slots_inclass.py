import sys

# Class thông thường
class PointRegular:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Class sử dụng __slots__
class PointSlots:
    __slots__ = ('x', 'y')  # Cố định thuộc tính
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Hàm đo đạc bộ nhớ (ước tính)
def demo_memory():
    n = 1000000
    
    # Tạo 1 triệu đối tượng Regular
    points_regular = [PointRegular(i, i) for i in range(n)]
    print("")
    # Chúng ta đo một đối tượng điển hình và nhân lên để thấy sự khác biệt quy mô
    size_reg = sys.getsizeof(points_regular[0]) + sys.getsizeof(points_regular[0].__dict__)
    print("day la size_reg")
    print(size_reg)
    # Tạo 1 triệu đối tượng Slots
    points_slots = [PointSlots(i, i) for i in range(n)]
    size_slots = sys.getsizeof(points_slots[0])

    print(f"--- Kết quả cho {n} đối tượng ---")
    print(f"Regular Class: ~{size_reg * n / 1024 / 1024:.2f} MB")
    print(f"Slots Class:   ~{size_slots * n / 1024 / 1024:.2f} MB")
    print(f"Tiết kiệm được: ~{100 - (size_slots/size_reg*100):.1f}% bộ nhớ")

demo_memory()