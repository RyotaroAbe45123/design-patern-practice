class Base(object):
    def __new__(self, *args, **kwargs):
        if not hasattr(self, "_instance"):
            self._instance = super(Base, self).__new__(self)
        return self._instance


class Singleton(Base):
    def __init__(self, value: int):
        self.__value = value
        print(self.__value)