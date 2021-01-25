a = "qwerty"
b = [1,2,3]
c = (4, 5, 6)



class MyIteratorCreator:
    def __init__(self, start=0, end=5, flag='int'):
        self.flag = flag
        self.item = start
        self.end = end

    def __iter__(self):
        if self.flag == 'int':
            return MyIterator(self.item, self.end)
        else:
            return MyIterator2(self.item, self.end)



class MyIterator:

    def __init__(self, start=0, end=5):
        self.item = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.item += 1
        if self.item < self.end:
            return self.item
        else:
            raise StopIteration


class MyIterator2:
    def __init__(self, start=0, end=5):
        self.item = start
        self.end = end

    def __next__(self):
        self.item += 1
        if self.item < self.end:
            return chr(self.item)
        else:
            raise StopIteration



my_counter = MyIteratorCreator(67,93, flag='int')
for i in my_counter:
    print(i)