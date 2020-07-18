'''
Created on Sep 22, 2018

@author: luis
'''
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
    def __init__(self):
        self.data = []
    
x=MyClass()
print(x.i)
print(x.f())
print(x.__doc__)