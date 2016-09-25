#######
#######
#######
#######
#######
#######
#######
####### Time Series Model for S&P 500
####### Compiled by Raul Eulogio
#######
#######
#######
#######
#######
#######


##
####
######
#     LOADING DATA, MODULES
######
####
##

# pandas
# numpy 
# statsmodel
# matplotlib

import pandas as pd
import numpy as np 
import statsmodels.api as sm  
from statsmodels.tsa.arima_model import ARIMA, ARIMAResults
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
#from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pylab as plt 
import csv
import matplotlib.dates as dates
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

##
####
######
#     TESTING that data loads properly
######
####
##
# 



# Recall that in order for the terminal to output txt write 
# python script.py > output.txt
# Also important recall to create a folder called 'images' for the plots to save in the correct directory!
dataMaster = pd.read_csv('sp_500_ts.csv')
sp_500 =  dataMaster['sp_500']
print "Here's our Original CSV file!"
print sp_500.head(12)
# Set the variable data as a date time object
ran = pd.date_range('1995-01', '2016-1', freq = 'M')
ts = pd.Series(dataMaster['sp_500'].values, index = ran)
print "This is the TS object!"
print ts.head(12)
print ts.dtypes
print "Output for our dataformat"
print ran


##
####
######
#     CREATING TIME-SERIES OBJECTS WITH FINANCIAL DATA 
######
####
##


# Testing to see if the object is a time series object!
print "Here is the year 2014"
print ts['2014']
print "This is the interval from 1995 to 2014:"
sp500_TR = ts['1995':'2014']
print sp500_TR
##
####
######
#     TIME SERIES STUFF
######
####
##


# Plotting the time series object 
plt.plot(ts)
plt.title('Time Series Plot of S&P 500')
plt.savefig("images/timeSeries.png", format = 'png') 
plt.close()

# Plotting Seasonal Decomposition 
# res = seasonal_decompose(sp_500)
# des = res.plot()
# des.savefig("images/seasonalDecomp.png", format = 'png')
# des.close()


# Plotting the time series object after being differenced
sp500_diff = ts - ts.shift()
diff = sp500_diff.dropna()
print "Here is our differenced time series"
print diff.head(12)

plt.plot(diff)
plt.title('First Difference Time Series Plot')
plt.savefig("images/timeSeriesDiff.png", format = 'png')
plt.close()




# Respective ACF and PACF plots for time series
acf = plot_acf(ts, lags = 20)
acf.savefig("images/timeSeriesACF.png", format = 'png')

pacf = plot_pacf(ts, lags = 20)
pacf.savefig("images/timeSeriesPACF.png", format = 'png')


# Respective ACF and PACF plots for first difference of time series
acfDiff = plot_acf(diff, lags = 20)
acfDiff.savefig("images/timeSeriesACFDiff.png", format = 'png')

pacfDiff = plot_pacf(diff, lags = 20)
pacfDiff.savefig("images/timeSeriesPACFDiff.png", format = 'png') 


##
####
######
#     ARIMA MODEL PREDICTIONS FOR 2014-15
######
####
##

mod = ARIMA(sp500_TR, order = (0, 1, 1), freq = 'M')

print "Our model summary"
results = mod.fit()
print results.summary()
print "Our predicted Values using predict on our ARIMA model!"
print results.predict(239, 251, typ='levels')
predVals = results.predict(239, 251, typ='levels')
# I dropped Dec 31, 2014 since I wasn't trying to predict this value and kept getting
# an error if I changed the indice as 240, 251!
predVals = predVals.drop(predVals.index[0])
print "Here are our predicted values!!!!!"
print predVals
# predVals = predVals.cumsum()
# print predVals
# Note: don't know how to include drift as the model including drift had better
# model accuracy 

# Here we plot the actual 2015 values vs the predicted values!
concan = pd.concat([ts, predVals], axis = 1, keys=['original', 'predicted'])
print "The data frame including the predicted values using ARIMA!"
print concan['2014':'2015']
ax = concan.plot()
fig = ax.get_figure()
fig.savefig('images/predVAct.png')

# Now we just zoom in to get a better picture
ax1 = concan.plot()
ax1.axis(['2014', '2016', 1800, 2200])
fig1 = ax1.get_figure()
fig1.savefig('images/predVActZoom.png')
# Last remarks: Couldn't find any documentation regarding adding 95% CI which I assume I will have to calculate manually. 
# Seasonal Decompostion doesn't seem to work. 
# There might be issues with when the dates are assigned i.e. for python I have dates as 1/31 etc while I am not 100% sure if this is an issue. 
# I can not some visual differences between R and python even though the predicted values are the same!

