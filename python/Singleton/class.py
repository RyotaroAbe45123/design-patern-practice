# https://qiita.com/TrashBoxx/items/7a76e46122191529c526
# classは実はtypeのインスタンスらしい！
class A:
    pass
print(type(A))

# python source code
# https://github.com/python/cpython/blob/3.10/Lib/abc.py

class B(object):
    def __new__(self, *args, **kwargs):
        if not hasattr(self, "__instance"):
            self.__instance = super().__new__(self)
        return self.__instance
        
    def __init__(self, v):
        print('init')
        self.v = v
        super().__init__()

print(B)
b = B(1)
print(b.v)
c = B(2)
print(b.v)
print(c.v)
print(b)
print(dir(b))
# print(b.__bool__)
print(b.__class__)
print(b.__delattr__)
print(b.__dir__)
print(b.__doc__)
print(b.__eq__)
print(b.__format__)
print(b.__ge__)
print(b.__getattribute__)
print(b.__gt__)
print(b.__hash__)
print(b.__init__)
print(b.__init_subclass__)
print(b.__le__)
print(b.__lt__)
print(b.__ne__)
print(b.__new__)
print(b.__reduce__)
print(b.__module__)
print(b.__reduce_ex__)
print(b.__repr__)
print(b.__setattr__)
print(b.__sizeof__())
print(b.__str__)
print(b.__subclasshook__)
