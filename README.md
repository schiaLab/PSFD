# PSFD Documentation

Developer: Hyeonjun Kim, Finance Q Institute, South Korea

## Functions

This simple python module enables you to analyze the phase space of a certain time series data. The module consist of three functions.
* `timeSeriesEmbedding(series:np.array, dim)`: This function receives a time series and integer dimension. Then the function returns the embedded space of the time series in given dimension. 
* `correlationIntegral(embeddedSpace:np.array, r)`: This function receives an embedded space of the time series and the threshold value. By given condition, the function returns the result of the correlation integral.
* `dimensionEstimate(embeddedSpace:np.array, start=1.001, end=2, num=50)` This function receives an embedded space of the time series and the start and end of possible threshold points and its number. Then, the function calculates correlation integral for each threshold point and then returns the fractal dimension of the phase space regressed from the data, and the loss that occurred during estimation of the fractal dimension. When `plot=True`, the function also shows you the plot of the regression.


## Discussion

### When do I use this module?

This module could be used specifically for analyzing dynamic variable originated from a complex system, such as the stock market or ECG. The orignial study that this module is based on focused on ECG data.

### What dimension is optimal for my analysis?

In short, it is highly likely that the optimal number will depends on your field. 

### What threshold interval is optimal for my analysis?

I might say that this also depends on your field. When I use this module for my study, I found that (1.001, 2) is the quite optimal interval. So make sure to test several intervals while the plotting option is on. When choosing wide enough interval, you might find the interval that shows the most linear relation, and where threshold value is too small or large. You might also have to consider that mathematically, changing the embedding dimension also effects the threshold interval.


## Reference

Lahiri, Tapobrata, et al. "Analysis of ECG signal by chaos principle to help automatic diagnosis of myocardial infarction." (2009).

