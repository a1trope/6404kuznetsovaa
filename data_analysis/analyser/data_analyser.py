from pandas import Series


def get_moving_average(series: Series, window_size: int):
    rolling_means = []

    for i in range(len(series)):
        if i < window_size - 1:
            tmp_size = i + 1
            window_sum = sum(series[0:i+1])
            rolling_mean = window_sum / tmp_size
        else:
            window_sum = sum(list(series[i - window_size + 1:i + 1]))
            rolling_mean = window_sum / window_size
        rolling_means.append(rolling_mean)

    rolling_mean_series = Series(rolling_means, index=series.index)
    return rolling_mean_series


def get_timeseries_differential(series: Series):
    return series.diff()


def get_autocorrelation(series: Series, lag: int = 1):
    return series.autocorr(lag=lag)
