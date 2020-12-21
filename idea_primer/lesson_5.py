import os
import copy
'./test.txt'
path = 'test.txt'
#path = os.path.join('Subdir', 'test.txt')
# f = open(path, 'r', encoding='UTF-8')

#-------------------- otkritie pravil'nioe ne nuzno pisat' close
# with open(path, 'r', encoding='UTF-8') as f:
#     print(f.read())
#------------------------------------------


#f.write('\nKamazov Vahvah')
##print(f.readlines())
# print(len(f.read()))
# f.close()

## rt - флаг указывающий что файл текстовый
## rb - флаг для открытия в двоичном формате

# my_list = [1,2,3,[3,5,6],7]
# new_list = copy.deepcopy(my_list)
# # new_list = my_list[:]
# new_list[3][0] = 5
# new_list[2] = 7
# print(my_list)
# print(new_list)
# print(id(my_list))
# print(id(new_list))

# fruits= ['Kiwi', 'Pineapple', 'Orange']
# result = True if 'Kiwi' in fruits else False
# # if 'Kiwi' in fruits:
# #     result= True
# print(result)

# def check(item):
#     return True if item[0] == 'P' else False
#
# fruits= ['Kiwi', 'Pineapple', 'Orange']
# result = filter(check, fruits)
# print(list(result))


# def check(item):
#     return True if item[0] == 'P' else False
# fruits= ['Kiwi', 'Pineapple', 'Orange']
# result = filter(lambda item: True if item[0] == 'P' else False, fruits)
# print(list(result))

fruits= ['Kiwi', 'Pineapple', 'Orange']
super_check = lambda name, array: True if name in array else False
print(super_check('Kiwi', fruits))

onw = [item*item for item in range(0,101, 5)]
two = tuple(item*item for item in range(0,101, 5))
print(two)

three= {i: chr(i) for i in range(65,91)}
print(three)
