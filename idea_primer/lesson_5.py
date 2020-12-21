'./test.txt'

path = './test.txt'
f = open(path, 'r', encoding='UTF-8')
##print(f.readlines())
print(f.read())
f.close()

## rt - флаг указывающий что файл текстовый
## rb - флаг для открытия в двоичном формате