data = [4,5,6,7]

a = iter(data)

print(f"this is {a} ")
print(f"this is next(a){next(a)}")
print(f"this is next(a){next(a)}")
data[2] = 9
print(f"this is next(a){next(a)}")
print(f"this is next(a){next(a)}")
print(f"this is next(a){next(a)}")

