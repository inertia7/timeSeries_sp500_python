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
# statsmodel
# matplotlib

import pandas as pd
import numpy as np 
import statsmodels.api as sm  
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pylab as plt 
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

#dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
# dataMaster = pd.read_csv('sp_500_ts.csv', parse_dates='Date', index_col='Date', date_parser=dateparse)
dataMaster = pd.read_csv('sp_500_ts.csv', skipinitialspace=True)


##
####
######
#     CREATING TIME-SERIES OBJECTS WITH FINANCIAL DATA 
######
####
##

sp_500 = dataMaster['sp_500'] 
print "This is the time series object"
print dataMaster.dtypes

##
####
######
#     TIME SERIES STUFF
######
####
##


# Plotting the time series object 
plt.plot(sp_500)
plt.title('Time Series Plot of S&P 500')
plt.savefig("images/timeSeries.png", format = 'png')
plt.close()

# Plotting the time series object after being differenced
sp500_diff = sp_500 - sp_500.shift()
diff = sp500_diff.dropna()
print
print diff

plt.plot(diff)
plt.title('First Difference Time Series Plot')
plt.savefig("images/timeSeriesDiff.png", format = 'png')
plt.close()




# Respective ACF and PACF plots for time series
acf = plot_acf(sp_500, lags = 20)
acf.savefig("images/timeSeriesACF.png", format = 'png')

pacf = plot_pacf(sp_500, lags = 20)
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

model = ARIMA(sp_500, order = (0, 1, 1))
# Note: don't know how to include drift as the model including drift had better
# model accuracy 
fit = model.fit(disp=-1)

fit = pd.Series(fit.fittedvalues, copy = True)
fit= fit.cumsum()
fit = fit

plt.figure()
plt.plot(sp_500)
plt.plot(fit)
plt.title('Fitted Vs. Actual Values for ')
plt.savefig ("images/realVPred.png", format = 'png')
plt.close()

# Next process is predicting a year ahead using our model 
# res = fit.forecast(steps = 12)
# res.savefig("forecastedPredictions.png", format = 'png')
