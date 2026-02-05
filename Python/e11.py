'''Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is,n = mi for some
integer i,andFalse otherwise.'''
def is_multiple(n,m): 
    while True: 
        try : 
            return n%m
        except ZeroDivisionError as e :
            print(f"Change m value {e}")
def main():
    n= int(input("Type n value : "))
    m= int(input("Type m values: "))
    if is_multiple(n,m) != 0 : 
        print(f"{n} is not multiple of {m} ")
    else:
        print(f"{n} is multiple of {m}")

if __name__ == "__main__":
    main()

