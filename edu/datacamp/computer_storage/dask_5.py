#  DASK

#  COMPOSING FUNCTIONS

from math import sqrt
import pandas as pd

from dask import delayed


def f(z):
    return sqrt(z + 4)


def g(y):
    return y - 3


def h(x):
    return x ** 2


x = 4
print(f(g(h(x))))  # Equal

x = 4
y = h(x)
z = g(y)
w = f(z)

print(w)  # Final result


#  DEFERRING COMPUTATION WITH DELAYED

from dask import delayed

y = delayed(h)(x)
z = delayed(g)(y)
w = delayed(f)(z)
print(w)

'''
    Delayed('f-5f9307e5-eb43-4304-877f-1df5c583c11c')
'''

type(w)  # a dask Delayed object

'''
    dask.delayed.Delayed
'''

w.compute() # Computation occurs now

'''
    4.123105625617661
'''

#   VISUALIZING A TASK GRAPH

w.visualize()


#   RENAMING DECORATED FUNCTIONS

f = delayed(f)
g = delayed(g)
h = delayed(h)
w = f(g(h(4)))

type(w)

'''
    dask.delayed.Delayed
'''

w.compute() # Computation occurs now

#   USING DECORATOR @-NOTATION

def f(x):
    return sqrt(x + 4)
f = delayed(f)

@delayed # Equivalent to definition in above 2 cells
def f(x):
    return sqrt(x + 4)

#  DEFERRING COMPUTATION WITH LOOPS

@delayed
def increment(x):
    return x+1

@delayed
def double(x):
    return 2 * x

@delayed
def add(x, y):
    return x+y

data = [1, 2, 3, 4, 5]
output = []
for x in data:
    a = increment(x)
    b = double(x)
    c = add(a, b)
    output.append(c)

total = sum(output)
print(f'EL total es: {total}')


#   AGGREGATING WITH DELAYED FUNCTIONS

template ='yellow_tripdata_2015-{:02d}.csv'
filenames = [template.format(k) for k in range(1,13)]
@delayed
def count_long_trips(df):
    df['duration'] = (df.tpep_dropoff_datetime - df.tpep_pickup_datetime).dt.seconds
    is_long_trip = df.duration > 1200
    result_dict = {'n_long':[sum(is_long_trip)],
    'n_total':[len(df)]}
    return pd.DataFrame(result_dict)

@delayed
def read_file(fname):
    return pd.read_csv(fname, parse_dates=[1,2])

#  COMPUTING FRACTION OF LONG TRIPS WITH DELAYED FUNCTIONS

totals = [count_long_trips(read_file(fname)) for fname in filenames]
annual_totals = sum(totals)
annual_totals = annual_totals.compute()

'''
    n_long n_total
0 172617 851390
    
'''

fraction = annual_totals['n_long']/annual_totals['n_total']
print(fraction)

'''
    0   0.202747
dtype: float64
'''


