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
from matplotlib import pyplot as py

### Change working directory if needed
import os
os.chdir("C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507ProjectTwo/data/")
os.getcwd()

#data = Orange.ExampleTable("housing")
#data=Orange.data.Table("housing")

# Bring in the data using the C4.5 format, which brings in the .data file and then the .names file
data = orange.ExampleTable("housing")
print data.domain.attributes

names=str(data.domain).replace('[','').replace(']','').split(',')
# Make Scatterplots of all the variables versus the target variable
def scatterplot(data, data_name, target_var):
    import matplotlib.pyplot as plt
    M = len(data[0])-1
    N=len(data)
    fig = plt.figure()

    y=[float(data[l][target_var]) for l in range(N)]

    for i in range(M):
        ax = fig.add_subplot(int(M/4.)+1,4,i+1)
        py.setp(ax.get_xticklabels(), visible=False)
        x=[float(data[k][i]) for k in range(N)]
        ax.scatter(x,y)
        #ax.set_xlabel(data_name[i],size='10')
        ax.set_title(data_name[i],size='10')
        #ax.set_ylabel(data_name[target_var],size='10')
    return fig
fig = scatterplot(data, names, len(data[0])-1)
fig.savefig('C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507ProjectTwo/data/scatter.png')
    


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

os.chdir("C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507ProjectTwo/src/")
from earth_example import rss
X, Y = data.to_numpy("A/C")

y_1=rss(Y,y_hat)
Orange.regression.earth.plot_evimp(earth_predictor.evimp())

# Compute using the standard regression model
import ols
model=ols.ols(Y,X,names[len(names)-1],names[:len(names)-1])
model.summary()
# Get the regression coefficients
coeff=model.b
# Score the data
y_hat_ols=[]
for i in range(len(data)):
    y_hat=coeff[0]
    for j in range(len(coeff)-1):
        #print coeff[j+1]
        #print data[i][j]
        y_hat=y_hat+data[i][j]*coeff[j+1]
    y_hat_ols.append(y_hat)
# Compute the RSS
y_2=rss(Y,y_hat_ols)
        




