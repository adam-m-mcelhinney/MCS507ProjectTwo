"""
Implementation of the MARS algorithm
"""
import Orange
import orange
from Orange.regression import earth
import os
import numpy as np
from scipy import stats


### Change working directory if needed

os.chdir("C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507ProjectTwo/data/")
print os.getcwd()

# Bring in the data 
data = orange.ExampleTable("example_data")

#Split data into response array and x values
x_col=0
y_col=1
dat=list(data)
x=[]
y=[]
for i in range(0,len(dat)-1):
    x.append(float(dat[i][x_col]))
    y.append(float(dat[i][y_col]))


y_bar=np.mean(y)
x_bar=np.mean(x)



def rss(y,y_hat):
    """
    Computes the Residual Sum of Squares
    """
    res=[]
    for i in range(0,len(y)-1):
        res.append((y[i]-y_hat[i])**2)
    rss=sum(res)
    return rss

r=rss(y,x)


slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

def knot(x,y):
    """
    Finds the optimal location of the knot
    """
    model=[]
    
    




        
    
