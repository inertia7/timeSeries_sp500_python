# Forecasting The Stock Market (Python)
## Time-Series Analysis of the S&P 500 Stock Index with **Python**
(Project can be found at: http://www.inertia7.com/projects/time-series-stock-market-python)

## Table of Contents

* [Abstract](#Abstract)
* [Contributors](## Contributors)

## <a name="Abstract"></a>Abstract
This project focuses on deriving the best statistical-learning model to predict future values for the **S&P 500 Stock Index** with **Python**.

Understanding the **S&P 500 Stock Index** is highly-relevant in understanding the health of the U.S. economy as it is highly-correlated (statistically) with other U.S. economic indicators such as other stock indices (e.g. the NASDAQ Stock Index and the NYSE Stock Exchange), the U.S. Housing Price Index, and the U.S. Gross Domestic Product (U.S. GDP).

Time-series analysis is a basic concept within the field of statistical-learning, which is appropriate for the analysis of the **S&P 500 Stock Index**.

For this project we leverage the horse-power of Python and deliver, where appropriate, gorgeous data visualizations using **matplotlib**. Since this is an iteration of the time series analysis done in **R**, (see: http://www.inertia7.com/projects/time-series-stock-market-r) we will be iterating much of what we said on that project unto this project.

It is important to note that time series analysis in **Python** is still developing so this project is not as extensive as the **R** project, but we hope to provide sufficient resources to enable you to start a time series project in **Python**

## <a name="Contributors"></a>Contributors
- Raul Eulogio
- David A. Campos
- Vincent La

## Modules Required 
Here we included the modules needed to ensure the script runs smoothly:

	- pandas
	- numpy 
	- statsmodels
	- matplotlib

Before running the script we recommend using **pip** to install the modules. Here we show an example when running on **linux** (in our case **Ubuntu**)

	sudo pip install pandas

Where **Macs** and **Windows** follow a similar pattern, here we provided a reference to [using pip](https://packaging.python.org/installing/) if you need further help. 

The biggest difference that we would like to note, if you are swithcing over from **R** to **Python** is that when importing modules you have to specify functions from these modules. Whereas when loading the packages in **R**, all functions from the package become accessible, in **Python** you would use for example at the start of your script:

	 from statsmodels.tsa.arima_model import ARIMA

We wanted to note this because as novice **Python** users this was an issue we faced so we want to help with the process of transitioning from one language to another. 

## Steps Required

### Creating working directory
Before running the script we recommend creating  directory for your project if you have not done so, this will facilitate that our script will run smoothly as well as saving images correctly since we used the `savefig` function from **matplotlib**. Creating the parent directory along with the images subdirectory will prove to be useful in the long run for any projects you fork/reproduce from **GitHub** or any other online resource! 

For **Linux** and **mac** users, the following command wil create the appropriate parent directory and subdirectory:

	 mkdir -p /home/user/myProjects/timeSeriesPython/images

For this example, we put the project in the myProject directory, but you can put the project where ever you feel appropriate. 

# Methodology 
For our time series analysis, we chose to focus on the [Box-Jenkins](https://en.wikipedia.org/wiki/Box%E2%80%93Jenkins#Box-Jenkins_model_identification) methodology which incorporates a series of steps to ensure we  produce the best model to forecasting. We used the years 1995 to 2014, withholding 2015 so that we can compare the forecast.

But before we outline the steps we would like to outline some  necessary assumptions for univariate time series analysis:

- The Box-Jenkins Model assumes weakly stationarity process. 
- The residuals are white noise (independently and identically distributed random variables) and homoscedastic


We won't go into detail since there is already a plethora of online resources outlining these assumptions, but we did feel that it was important to state these assumptions.

## ARIMA Model 
(**NOTE**: We copy pasted most of the README from the [timeSeries_sp500_R](https://github.com/inertia7/timeSeries_sp500_R/blob/master/README.md) since they are similar projects but just in different languages.)

For this project we will be using the **Autoregressive Integrated Moving Average** model and its variations to forecast the S&P 500. For each component we have a corresponding variable for which we model if there is sign of these components. Here we roughly outline the parts that make an **ARIMA(p,d,q)** model 
- **Autoregressive [AR(p)]** - a stochastic process where future values are dependent on past values signifying that past values have a linear effect on the future values.
- **Integration [I(d)]** - when differencing is done to make a process stationary, we include the differenced value(i.e. if we took the first difference it would be I(d=1))
- **Moving Average [MA(q)]** - a prcoess where the current value is linearly regressed on current and past white noise terms (residuals)

Next we outline the steps to ensure we fit the appropriate **ARIMA(p,d,q)** model!

## Stationary process and Seasonality
The first step is checking to see if the time series object is stationary, this can be done in various methods which can also be explained as exploratory analysis since we are in essence "getting a feel" for our data.

## Autocorrelation and Partial Autocorrelation Plots
These plots play a crucial role in time series analysis, because we can estimate our **ARIMA(p,d,q)** model based on the behaviour of these plots or justify the need to do an appropriate transformation.  

We won't go into too much detail since we outlined the process in the project, but through the use of our ACF and PACF plots for our original time series we were able to make the deduction to take the first difference of our time series. Once we did that we saw that the ACF and PACF plot showed characteristics of a MA(1) model, but since we took the first difference it becomes a mixed model; **ARIMA(0, 1, 1)**

## Forecast
We forecasted using the **ARIMA(0,1,1)** model, but the biggest difference is that we did not include drift in this iteration because we did not any documentation that said this was readily available through the **statsmodels** module. 

We would like to state this project is iterative so we will be expanding to include more features that were on the **R** project. 
