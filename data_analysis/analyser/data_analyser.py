from pandas import DataFrame, Series


def get_moving_average(df: Series, window: int):
    return df.rolling(window=window)


def get_timeseries_differential(df: Series):
    raise NotImplementedError


def get_autocorrelation(df: Series, lag: int = 1):
    return df.autocorr(lag=lag)
