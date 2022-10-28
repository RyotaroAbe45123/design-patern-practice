class Base(object):
    def __new__(self, *args, **kwargs):
        if not hasattr(self, "_instance"):
            self._instance = super(Base, self).__new__(self)
        return self._instance


class _Singleton(Base):
    def __init__(self, value: int):
        self._value = value
        self.__value = value


class Singleton:
    __instance = None
    def __new__(self, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = super().__new__(self)
        return Singleton.__instance