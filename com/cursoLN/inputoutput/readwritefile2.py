with open('f','a') as f:
    value = ('the answer', 42)
    s = str(value)  # convert the tuple to string
    f.write(s)
f.closed
with open('f','r') as f:
    read_data = f.read()
    print(read_data)
f.closed
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)      # Go to the 6th byte in the file

print(f.read(1))

print(f.seek(-3, 2))  # Go to the 3rd byte before the end

print(f.read(1))