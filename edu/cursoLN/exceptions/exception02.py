'''
Created on Sep 17, 2018

@author: luis
'''

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
        
'''
Note that if the except clauses were reversed (with except B first), 
it would have printed B, B, B — the first matching except clause is triggered.

'''