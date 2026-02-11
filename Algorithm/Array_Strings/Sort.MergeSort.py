def merge_sort(arr):
    if len(arr) > 1:
        # Chia m?ng ra 2 n?a
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # ?? quy sort t?ng n?a
        merge_sort(left)
        merge_sort(right)

        # Tr?n hai n?a ?ã ???c sort l?i
        i = j = k = 0

        # So sánh t?ng ph?n t? t? hai n?a và ??a vào m?ng chính
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # N?u còn ph?n t? ? left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # N?u còn ph?n t? ? right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Dùng th?
arr = [38, 27, 43, 3, 9, 82, 10]
print("M?ng ban ??u:", arr)
merge_sort(arr)
print("M?ng sau khi s?p x?p:", arr)
