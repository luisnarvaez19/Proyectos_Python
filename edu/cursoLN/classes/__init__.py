'''
    I'm actually surprised this isn't a duplicate. I saw some similar questions
    and I think there is nowhere a concise answer, so here is how I do it:

    Class (or group of) is actually a full module. You don't have to do it this way,
    but if you're splitting a class on multiple files I think this is 'cleanest' (opinion).
    The definition is in __init__.py, methods are split into files by a meaningful grouping.

    A method file is just a regular python file with functions, except you can't forget
    'self' as a first argument. You can have auxiliary methods here, both taking self and not.
    Methods are imported directly into the class definition.

    Suppose my class is some fitting gui (this is actually what I did this for first time).
    So my file hierarchy may look something like

    mymodule/
         __init__.py
         _plotstuff.py
         _fitstuff.py
         _datastuff.py

    So plot stuff will have plotting methods, fit stuff contains fitting methods,
    and data stuff contains methods for loading and handling of data - you get the point.

    By convention I mark the files with a _ to indicate these really aren't meant to be imported
    directly anywhere outside the module.

    So _plotsuff.py for example may look like:

    def plot(self,x,y):
         #body
    def clear(self):
         #body
    etc. Now the important thing is __init__.py:

    class Fitter(object):
         def __init__(self,whatever):
             self.field1 = 0
             self.field2 = watever

         #Imported methods
         from ._plotstuff import plot, clear
         from ._fitstuff  import fit
         from ._datastuff import load
         from ._static_example import something

         #Some more small functions
         def printHi(self):
             print("Hello world")

         #static methods need to be set
         somthing = staticmethod(something)

    Tom Sawyer mentions PEP-8 recommends putting all imports at the top, so you may wish
    to put them before __init__, but I prefer it this way. I have to say, my Flake8
    checker does not complain, so likely this is PEP-8 compliant.

    Note the from ... import ... is particularly useful to hide some 'helper'
    functions to your methods you don't want accessible through objects of the class.
    I usually also place the custom exceptions for the class in the different files,
    but import them directly so they can be accessed as Fitter.myexception.

    If this module is in your path then you can access your class with

    from mymodule import Fitter
    f = Fitter()
    f.load('somefile') #Imported method
    f.plot()           #Imported method

    Not completely intuitive, but not to difficult either. The short version for your
    specific problem was your were close - just move the import into the class, and use

    from separate import long_func_1
    and don't forget your self!


'''