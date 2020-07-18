"""
    list.extend(iterable)
    Lists
    languages=['C++','Python','Scratch']
    list1=[1,[2,3],(4,5),False,'No']

    Tuples
    colors=('Red','Green','Blue')

    Set
    DrakeSongs_set = {'In my feelings', 'Mia'}

    Lists and tuples are standard Python data types that store values
    in a sequence. Sets are another standard Python data type that
    also store values. The major difference is that sets, unlike lists
    or tuples, cannot have multiple occurrences of the same element
    and store unordered values.

    This Python Data Structure is like a, like a list in Python, is a
    heterogeneous container for items. But the major difference between
    the two (tuple and list) is that a list is mutable, but a tuple is
    immutable. This means that while you can reassign or delete an entire
    tuple, you cannot do the same to a single item or a slice.


    Finally, we will take a look at Python dictionaries. Think of a real-life
    dictionary. What is it used for? It holds word-meaning pairs. Likewise,
    a Python dictionary holds key-value pairs. However, you may not use an
    unhashable item as a key.

    To declare a Python dictionary, we use curly braces. But since it has
    key-value pairs instead of single values, this differentiates a dictionary
    from a set.

     {1: 2, 2: 4, 3: 6}


"""

# app.py

GoT = ['Daenerys', 'Jon', 'Tyrion']
Friends = ['Rachel', 'Monica', 'Phoebe']
GoT.extend(Friends)
print(GoT)

#  Let us extend a tuple to the list.

GoT1_list = ['Daenerys', 'Jon', 'Tyrion']
Friends1_tuple = ('Rachel', 'Monica', 'Phoebe')
GoT1_list.extend(Friends1_tuple)
print(GoT1_list)

# Add Elements of Set To List

MJSongs_list = ['Dangerous', 'Smooth criminal', 'Bad']
DrakeSongs_set = {'In my feelings', 'Mia'}
MJSongs_list.extend(DrakeSongs_set)
print(MJSongs_list)