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
import numpy as np 
import statsmodels.api as sm  
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pylab as plt 
from matplotlib.pylab import rcParams


##
####
######
#     TESTING that data loads properly
######
####
##
# 
# 


# Recall that in order for the terminal to output txt write 
# python script.py > output.txt

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

sp_500 = data['sp_500'] 

print sp_500

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
plt.savefig("timeSeries.png", format = 'png')
plt.close()

# Plotting the time series object after being differenced
sp500_diff = sp_500 - sp_500.shift()
diff = sp500_diff.dropna()
print
print diff

plt.plot(diff)
plt.title('First Difference Time Series Plot')
plt.savefig("timeSeriesDiff.png", format = 'png')
plt.close()




# We grab the acf and pacf for the time series with plot_acf and plot_pacf
# NOTE: Since I am in th process of getting acquainted I know that plot_acf outputs 'fig'
# this means I can run the same functionalities as plt!! 
acf = plot_acf(sp_500, lags = 20)
acf.savefig("timeSeriesACF.png", format = 'png')



pacf = plot_pacf(sp_500, lags = 20)
pacf.savefig("timeSeriesPACFDiff.png", format = 'png')


acfDiff = plot_acf(diff, lags = 20)
acfDiff.savefig("timeSeriesACFDiff.png", format = 'png')


pacfDiff = plot_pacf(diff, lags = 20)
pacfDiff.savefig("timeSeriesPACFDiff.png", format = 'png')


##
####
######
#     ARIMA MODEL PREDICTIONS FOR 2014-15
######
####
##

model = ARIMA(sp_500, order = (0, 1, 1))
fit = model.fit(disp=-1)

fit = pd.Series(fit.fittedvalues, copy = True)
fit= fit.cumsum()
fit = fit

plt.plot(sp_500)
plt.plot(fit)
plt.title('Fitted Vs. Actual Values for ')
plt.savefig("realVPred.png", format = 'png')
plt.close()
