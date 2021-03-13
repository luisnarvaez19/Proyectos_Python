'''
Created on Oct 6, 2018
Modified on on Sep 3, 2019
@author: luis
'''

import matplotlib.pyplot as plt
import numpy as np

xs = [0, 1, 2, 3, 4, 5, 6, 7]
ys = [1, 0.3, -2.3, 5.1, 7.6, -0.2, -1.8, 4]

plt.plot(xs, ys)
plt.show()



"""
Hay que arreglarlo no sirve
Plotting with categorical variables
It is also possible to create a plot using categorical variables.
 Matplotlib allows you to pass categorical variables directly to many plotting functions. 
"""
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(12, 5))
plt.plot(values)
plt.show()
"""
Typical call signature:

subplot(nrows, ncols, plot_number)
Where nrows and ncols are used to notionally split the figure into nrows * ncols sub-axes, 
and plot_number is used to identify the particular subplot that this function is to create 
within the notional grid. plot_number starts at 1, increments across rows first and has a
 maximum of nrows * ncols.

In the case when nrows, ncols and plot_number are all less than 10, a convenience exists,
 such that the a 3 digit number can be given instead, where the hundreds represent nrows,
  the tens represent ncols and the units represent plot_number. For instance:

subplot(211)
produces a subaxes in a figure which represents the top plot (i.e. the first) in a 2 row
 by 1 column notional grid (no grid actually exists, but conceptually this is how the 
 returned subplot has been positioned).
 
"""
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

