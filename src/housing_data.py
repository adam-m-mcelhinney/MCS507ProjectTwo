"""
Test the Mars Technique on the Bosting Housing Data Set
http://archive.ics.uci.edu/ml/datasets/Housing
http://orange.biolab.si/doc/reference/Orange.regression.earth/
http://orange.biolab.si/blog/2011/12/20/earth-multivariate-adaptive-regression-splines/
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

#data = Orange.ExampleTable("housing")
#data=Orange.data.Table("housing")

# Bring in the data using the C4.5 format, which brings in the .data file and then the .names file
data = orange.ExampleTable("housing")
print data.domain.attributes


def get_var_names(att):
    names=[]
    for i in range(0,len(att)):
        st=str(list(data.domain.attributes)[i]).split('\'')
        print st
        names.append(st[1])
    return names

names=get_var_names(data.domain.attributes)
    


# View the data
for i in range(5):
    print data[i]


earth_predictor = earth.EarthLearner(data)

print earth_predictor

dl=list(data)

# Predict all the data
y_hat=[]
for i in range(0,len(dl)):
    t=earth_predictor.predict(dl[i])
    y_hat.append(t[0])



X, Y = data.to_numpy("A/C")
for i in range(0,len(names)):
    print i
    pl.plot(X[:,i],Y, ".r")
    X_dat=list(X[:,i])
    pl.plot(X_dat,y_hat, ".b")
    pl.title(names[i])
    pl.show()
    
#Orange.regression.earth.plot_evimp(earth_predictor.evimp())
