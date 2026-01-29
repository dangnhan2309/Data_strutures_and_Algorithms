# 1. Khởi tạo một danh sách
original_list = [10, 20, 30]

# 2. Tạo một Alias (Bí danh)
alias_list = original_list 

# 3. Thay đổi giá trị thông qua Alias
alias_list.append(99)
alias_list[0] = "Python"

# 4. Kiểm tra kết quả
print(f"Original: {original_list}")
print(f"Alias:    {alias_list}")

# 5. Kiểm tra ID (địa chỉ vùng nhớ)
print(f"ID Original: {id(original_list)}")
print(f"ID Alias:    {id(alias_list)}")