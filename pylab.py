#!/usr/bin/env python
import numpy as np
import pylab as pl

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)

# the histogram of the data
n, bins, patches = pl.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = pl.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--', linewidth=1)

pl.xlabel('Smarts')
pl.ylabel('Probability')
pl.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
pl.axis([40, 160, 0, 0.03])
pl.grid(True)

pl.show()

