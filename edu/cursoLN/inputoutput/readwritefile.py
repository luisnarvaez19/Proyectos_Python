'''
    The with statement allows objects like files to be used in a way that
     ensures they are always cleaned up promptly and correctly.
     After the statement is executed, the file f is always closed, even if a 
     problem was encountered while processing the lines. Objects which, like 
     files, provide predefined clean-up actions will indicate this in their documentation.
'''
with open('f') as f:
    read_data = f.readline()
    print(read_data)
    read_data = f.readline()
    print(read_data)
f.closed
with open('f') as f:
    for line in f:
        print(line, end='')
f.closed
with open('f') as f:
    archivo=list(f)
    print(archivo)
f.closed
with open('f') as f:
    archivo=f.readlines()
    print(archivo)
f.closed
with open('f','r+') as f:
    f.write('Linea al final\n')
    read_data = f.read()
    print(read_data)
f.closed
with open("f") as f:
    for line in f:
        print(line, end="")
