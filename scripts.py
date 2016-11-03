####################################################
##
##		IMPORT MODULES
##
####################################################

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA, ARIMAResults
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pylab as plt
import matplotlib.dates as dates
from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 15, 6


####################################################
##
##		LOAD DATA
##
####################################################

# loading data

dataMaster = pd.read_csv('sp_500_ts.csv')
sp_500 = dataMaster['sp_500']

print sp_500.head(12)

ran = pd.date_range('1995-01', '2016-1', freq = 'M')
ts = pd.Series(dataMaster['sp_500'].values, index = ran)

print ts.head(12)

print ts.dtypes

####################################################
##
##		DO EXPLORATORY ANALYSIS
##
####################################################

plt.plot(ts)
plt.title('Time Series Plot for S&P 500')
# plt.xlim([0, 255])
plt.show()

sp500_TR = ts['1995':'2014']
print sp500_TR


####################################################
##
##		MODEL ESTIMATION
##
####################################################


# DIAGNOSING ACF

acf = plot_acf(ts, lags = 20)
plt.title("ACF Plot of SP 500")
acf.show()

# DIAGNOSING PACF

pacf = plot_pacf(ts, lags = 20)
plt.title("PACF Plot of SP 500")
pacf.show()

# TRANSFORMING OUR DATA TO ADJUST FOR NON-STATIONARITY

sp500_diff = ts - ts.shift()
diff = sp500_diff.dropna()
print diff.head(12)
print diff.dtypes

plt.figure()
plt.plot(diff)
plt.title('First Difference Time Series Plot')
plt.show()

acfDiff = plot_acf(diff, lags = 20)
plt.title("ACF Plot of S 500(Difference)")
acfDiff.savefig("images/timeSeriesACFDiff.png", format = 'png')
acfDiff.show()

# edit this shit on the actual project !
pacfDiff = plot_pacf(diff, lags = 20)
plt.title("PACF Plot of SP 500(Difference)")
pacfDiff.savefig("images/pacfDiff.png", format = 'png')
pacfDiff.show()

####################################################
##
##		BUILD MODEL
##
####################################################

mod = ARIMA(sp500_TR, order = (0, 1, 1), freq = 'M')

results = mod.fit()
print results.summary()

####################################################
##
##		FORECAST
##
####################################################

predVals = results.predict(239, 251, typ='levels')
print predVals

predVals = predVals.drop(predVals.index[0])
print predVals

sp500_for = pd.concat([ts, predVals], axis = 1, keys=['original', 'predicted'])
print sp500_for['2014':'2015']

plt.figure()
plt.plot(sp500_for)
plt.title("Actual Vs. Forecasted Values")
plt.savefig("images/sp500_for.png", format = 'png')
plt.show()

plt.figure()
plt.plot(sp500_for)
plt.title('Real Vs. Predicted Values for 2015')
plt.savefig("images/sp500_for2.png", format = 'png')
plt.show()
