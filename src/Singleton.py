'''
Singleton class borrowed from: 
https://sourcemaking.com/design_patterns/singleton/python/1
Define an Instance operation that lets clients access its unique
instance.
'''
class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance