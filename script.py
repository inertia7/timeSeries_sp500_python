#######
#######
#######
#######
#######
#######
#######
####### Time Series Model for S&P 500
#######
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
# matplotlib
# plotly
# statsmodel

import pandas as pd
import plotly 
from plotly.graph_objs import *
import plotly.plotly as py 
import numpy as np 
import statsmodels.api as sm  
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pylab as plt 
from matplotlib.pylab import rcParams
plotly.tools.set_credentials_file(username = 'user', api_key = 'password')



##
####
######
#     TESTING that data loads properly
######
####
##
# fig, ax = plt.subplots( nrows=1, ncols=1)
# print data.head()




dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('sp_500_ts.csv', parse_dates='Date', index_col='Date', date_parser=dateparse)
print data.head()


##
####
######
#     CREATING TIME-SERIES OBJECTS WITH FINANCIAL DATA 
######
####
##

ts = data['sp_500'] 

print ts

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
plt.savefig("timeSeries.png", format = 'png')
plt.close()

# Plotting the time series object after being differenced
ts_diff = ts - ts.shift()
ts_diff = ts_diff.dropna()
print "This is the one with Pandas!"
print ts_diff

plt.plot(ts_diff)
plt.title('First Difference Time Series Plot')
plt.savefig("timeSeriesDiff.png", format = 'png')
plt.close()




# Test try of plot_acf
acf = plot_acf(ts, lags = 20)
acf.savefig("timeSeriesACF.png", format = 'png')



pacf = plot_pacf(ts, lags = 20)
pacf.savefig("timeSeriesPACFDiff.png", format = 'png')


acfDiff = plot_acf(ts_diff, lags = 20)
acfDiff.savefig("timeSeriesACFDiff.png", format = 'png')


pacfDiff = plot_pacf(ts_diff, lags = 20)
pacfDiff.savefig("timeSeriesPACFDiff.png", format = 'png')


##
####
######
#     ARIMA MODEL PREDICTIONS FOR 2014-15
######
####
##

model = ARIMA(ts, order = (0, 1, 1))
fit = model.fit(disp=-1)

fit = pd.Series(fit.fittedvalues, copy = True)
fit= fit.cumsum()
fit = fit

plt.plot(ts)
plt.plot(fit)
plt.title('Fitted Vs. Actual Values for ')
plt.savefig("realVPred.png", format = 'png')
plt.close()
