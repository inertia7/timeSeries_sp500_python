# Forecasting The Stock Market (Python)
## Time-Series Analysis of the S&P 500 Stock Index with **Python**
(Project can be found at: http://www.inertia7.com/projects/time-series-stock-market-python)

## Abstract
This project focuses on deriving the best statistical-learning model to predict future values for the **S&P 500 Stock Index** with **Python**.

Understanding the **S&P 500 Stock Index** is highly-relevant in understanding the health of the U.S. economy as it is highly-correlated (statistically) with other U.S. economic indicators such as other stock indices (e.g. the NASDAQ Stock Index and the NYSE Stock Exchange), the U.S. Housing Price Index, and the U.S. Gross Domestic Product (U.S. GDP).

Time-series analysis is a basic concept within the field of statistical-learning, which is appropriate for the analysis of the **S&P 500 Stock Index**.

For this project we leverage the horse-power of Python and deliver, where appropriate, gorgeous data visualizations using **matplotlib**. Since this is an iteration of the time series analysis done in **R**, (see: http://www.inertia7.com/projects/time-series-stock-market-r) we will be iterating much of what we said on that project unto this project.

It is important to note that time series analysis in **Python** is still developing so this project is not as extensive as the **R** project, but we hope to provide sufficient resources to enable you to start a time series project in **Python**

## Contributors
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

