import os
i = None
d = os.listdir(os.getcwd())
directory = os.getcwd()
print(d)
print('Список папок в текущей директории:')
for i in d:
    tmp_var = directory = os.getcwd() + '\\' + str(i)
    if os.path.isdir(tmp_var):
        print(i, end=' ')