"""
Example of "Earth" statistical analysis
http://orange.biolab.si/blog/2011/12/20/earth-multivariate-adaptive-regression-splines/
"""
import Orange,numpy, os, orange
from Orange.regression import earth
from matplotlib import pylab as pl
from numpy import polyfit, array, poly1d


# Change working directory to get data
os.chdir("C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507ProjectTwo/data/")


# Remember to add the "class" keyword to the third line, under the target variable. See here:
# http://orange.biolab.si/doc/tutorial/load-data/
data = orange.ExampleTable("painted_data_wo_outlier")
print data.domain.attributes
print data[:4]

X, Y = data.to_numpy("A/C")

pl.plot(X, Y, ".r")
pl.title('Example Data Set')
pl.show()

earth_predictor = earth.EarthLearner(data)
print earth_predictor
linspace = numpy.linspace(min(X), max(X), 20)
predictions = [earth_predictor([s, "?"]) for s in linspace]
pl.plot(X, Y, ".r")
pl.plot(linspace, predictions, "-b")
pl.title('Example Data Set with Line Fit by MARS')
pl.show()


x=[]; y=[]
for i in range(len(X)):
    #print i
    x.append(float(X[i]))
    y.append(float(Y[i]))


# 3rd, 4th, 5th degree polys
p3=polyfit(x,y,3)
pp3=poly1d(p3)

p4=polyfit(x,y,4)
pp4=poly1d(p4)

p5=polyfit(x,y,5)
pp5=poly1d(p5)

pl.plot(X, Y, ".r")
pl.plot(linspace, predictions, "-b")
pl.plot(linspace,pp3(linspace),"-g")
pl.plot(linspace,pp4(linspace),"-m")
pl.plot(linspace,pp5(linspace),"-y")
pl.title('Example Data Set with Line Fit by MARS and Higher Order Polynomials')
pl.legend(['Data','Mars','3rd Degree','4th Degree','5th Degree'],loc=2)
pl.show()

# Create function to calc RSS
def rss(y_obs, y_predicted):
    r=0
    for i in range(len(y_obs)):
        t=(y_obs[i]-y_predicted[i])**2.
        r=r+t
    return r

# Calc RSS for all models
y_predicted1=[earth_predictor([X[i], "?"]) for i in range(len(X))]
y_predicted3=pp3(X)
y_predicted4=pp4(X)
y_predicted5=pp5(X)

r1=rss(Y,y_predicted1)
r3=rss(Y,y_predicted3)
r4=rss(Y,y_predicted4)
r5=rss(Y,y_predicted5)
