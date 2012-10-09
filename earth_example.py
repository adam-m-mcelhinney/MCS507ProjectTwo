"""
Example of "Earth" statistical analysis
http://orange.biolab.si/blog/2011/12/20/earth-multivariate-adaptive-regression-splines/
"""
import Orange
from Orange.regression import earth
#help(earth.EarthLearner)

import numpy
from matplotlib import pylab as pl


data = Orange.data.Table("data.tab")
earth_predictor = earth.EarthLearner(data)

X, Y = data.to_numpy("A/C")

pl.plot(X, Y, ".r")

linspace = numpy.linspace(min(X), max(X), 20)
predictions = [earth_predictor([s, "?"]) for s in linspace]

pl.plot(linspace, predictions, "-b")
pl.show()
