# https://qiita.com/TrashBoxx/items/7a76e46122191529c526
# classは実はtypeのインスタンスらしい！
class A:
    pass
print(type(A))

# python source code
# https://github.com/python/cpython/blob/3.10/Lib/abc.py