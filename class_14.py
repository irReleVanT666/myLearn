from typing import Union, Iterable

def modify_multi(x):
    return x * 2

def modify_pow(x):
    return x * 2

def my_map(seq: Iterable, func_obj) -> Iterable:
    new_seq = []
    for item in seq:
        new_seq.append(func_obj(item))

    return type(seq)(new_seq)



# result = my_map([1,2,3], modify)
# result2 =my_map((1,2,3), modify)



