import numpy as np
import pandas as pd

from com.datacamp.computer_storage.primero_1 import memory_footprint
before = memory_footprint()

N = (1024 ** 2 ) // 8 # Number of floats that fill 1 MB
x = np.random.rand(50*N)  # Random array filling 50 MB
after = memory_footprint()

print('Memory before: {} MB'.format(before))

print('Memory after: {} MB'.format(after))

before = memory_footprint()

x ** 2  # Computes, but doesn't bind result to a variable

after = memory_footprint()

print('Memory before: {} MB'.format(before))

print('Memory after: {} MB'.format(after))

print(x.nbytes // 1024 ** 2)

df = pd.DataFrame(x)

print(df.memory_usage(index=False))