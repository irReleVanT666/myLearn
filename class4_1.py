# def my_len(array):
#     if not isinstance(array, list):
#         print("!111")
#         return None
#     my_count = 0
#     for _ in array:
#         my_count += 1
#     return my_count

def say_hello(name=None):
    if name is None:
        name = input('Enter your Name:')
    print(f'Heklow, {name}!')

# say_hello()
# a = [1, 2, 3, 4, 'five', True, 0.5]
# c = my_len(True)
# print(c)
# c = my_len([1,2,3,4,5,6])
#
# def summ(a , b, c=0)

say_hello()