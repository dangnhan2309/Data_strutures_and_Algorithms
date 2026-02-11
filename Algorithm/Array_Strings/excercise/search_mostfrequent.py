from collections import Counter
arr=[1,2,2,5,4,6,3,6,898,2,4,222]
def search_mostfrequent(arr):
    counter = Counter(arr)
    most_common = counter.most_common(1)
    return most_common[0] if most_common else None
print(search_mostfrequent(arr))S