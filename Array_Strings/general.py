#Common operations: insert, delete, update, search
#LISt

import array
import numpy as np

def innit_list():
    list_ = [1,2,3,4,5,6,7,8]
    return array
def funtion_list(array):
    print(array)
    array.append(9)
    print(f"append 9 : {array}")
    array.remove(1)
    print(f"remove(1) : {array}")
    array.insert(2, 10)
    print(f"insert 2, 10 : {array}")

#Array library 
def innit_list():
    list_ = array.array('i',[1,2,3,4,5,6])
    return list_
def funtion_array(array):
    print(array)
    array.append(9)
    print(f"append 9 : {array}")
    array.remove(1)
    print(f"remove(1) : {array}")
    array.insert(2, 10)
    print(f"insert 2, 10 : {array}")

#Numpy Arrays
def innit_np():
    np_arr = np.array([1,2,3,4,5,6])
    return np_arr
#matrix Array 
def innit_list():
    list_ = [[1,1,1],[0,0,0]]
    return list_



def funtion_np(np_arr):
    print(np_arr)
    np_arr = np.append(np_arr, 9)
    print(f"append 9 : {np_arr}")
    np_arr = np.delete(np_arr, 1)
    print(f"remove(1) : {np_arr}")
    np_arr = np.insert(np_arr, 2, 10)
    print(f"insert 2, 10 : {np_arr}")

def innit_tuple():
    tuple_ = (1,2,3,4,5,6)
    return tuple_
def funtion_tuple(tuple_):
    show_list(tuple_)
    tuple_.append(9)
    show_list(tuple_)

def show_list(list_):
    print(list_)

def main():
    try:
     tuple_test = innit_tuple()
     funtion_tuple(tuple_test)
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()