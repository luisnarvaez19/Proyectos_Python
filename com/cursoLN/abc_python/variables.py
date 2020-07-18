#!/usr/bin/env cursoLN

a = 0

def foobar():
    #  Si se quita esta linea de global da error el codigo
    global a
    a = a + 2
    print(a)

foobar()

