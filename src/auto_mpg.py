"""
Test the Mars Technique on the Auto Mpg Data Set

http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/
"""

import csv
import Orange
import orange
from Orange.regression import earth
import numpy
from numpy import linspace
from matplotlib import pylab as pl

### Change working directory if needed
import os
os.chdir("C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507ProjectTwo/data/")
os.getcwd()



# Bring in the data using the C4.5 format, which brings in the .data file and then the .names file
data = orange.ExampleTable("auto-mpg")
print data.domain.attributes


# Divide data into training and validation data sets
index=Orange.data.sample.SubsetIndices2(p0=0.70)
ind=index(data)
data_training=data.select(ind,0)
data_validation=data.select(ind,1)


earth_predictor = earth.EarthLearner(data_training)

print earth_predictor

estimated=earth_predictor.predict(list(data_validation))


dl=list(data_validation)

# Predict all the data
estimated=[]
for i in range(0,len(dl)):
    t=earth_predictor.predict(dl[i])
    estimated.append(t[0])



X, Y = data.to_numpy("A/C")
for i in range(0,len(names)):
    print i
    pl.plot(X[:,i],Y, ".r")
    X_dat=list(X[:,i])
    pl.plot(X_dat,y_hat, ".b")
    pl.title(names[i])
    pl.show()
    
#Orange.regression.earth.plot_evimp(earth_predictor.evimp())
