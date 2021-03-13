'''
Created on Oct 6, 2018

@author: luis
'''

import math

import matplotlib.pyplot as plt
import numpy as np

# Create sinewaves with sine and cosine
xs = [i / 5.0 for i in range(0, 50)]
print(xs)
y1s = [math.sin(x) for x in xs]
y2s = [math.cos(x) for x in xs]

# Plot both sinewaves on the same graph
plt.plot(xs, y1s, 'r^', label='sin(x)')
plt.plot(xs, y2s, 'b--', label='cos(x)')

# Adjust the axes' limits: [xmin, xmax, ymin, ymax]
plt.axis([-1, 11, -1.5, 1.5])

# Give the graph a title and axis labels
plt.title('My Sinewaves')
plt.xlabel('Radians')
plt.ylabel('Value')

# Show a legend
plt.legend()

# Save the image
plt.savefig('sinewaves.png')

# Draw to the screen
plt.show()



import matplotlib.pyplot as plt
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])
plt.show()


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.legend()
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
