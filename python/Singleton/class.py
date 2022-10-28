# https://qiita.com/TrashBoxx/items/7a76e46122191529c526
# classは実はtypeのインスタンスらしい！
class A:
    pass
print(type(A))
print(dir(object))
print(object.__class__)
print(type(object))
print('------------------')

# python source code
# https://github.com/python/cpython/blob/3.10/Lib/abc.py

class B(object):
    def __new__(self, *args, **kwargs):
        print("new")
        if not hasattr(self, "__instance"):
            self.__instance = super().__new__(self)
        return self.__instance
        
    def __init__(self, v):
        print('init')
        self.v = v
        super().__init__()

class C:
    def __new__(self, *args, **kwargs):
        print("new")
        return object

class D(C):
    def __new__(self):
        print("new")
        return object
    def __init__(self) -> None:
        print("init")
        # super().__init__()

class E:
    def __new__(self, *args, **kwargs):
        print("new")
        instance = super().__new__(self)
        print(instance)
        print(type(instance))
        # return None
        # return instance
        b = B(1)
        return b

    # def __init__(self) -> None:
    def __init__(self, *args, **kwargs):
        print("init")
        # super().__init__()

print(C)
print(type(C))
c = C(1, {"a": 1})
print(c)
print('------------------')

print(D)
print(type(D))
d = D()
# d = D(1, {"a": 1})
print(d)
print('------------------')

print(E)
print(type(E))
e = E(1, {"a": 1})
print(e)
print('------------------==')


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
