import unittest
from data_analysis.analyser.data_analyser import get_moving_average
import pandas as pd


class TestGetMovingAverage(unittest.TestCase):
    def test_get_moving_average(self):
        data = [1, 3, 7, 1, 2, 8, 4, 6, 2]
        index = pd.date_range(start='2023-01-01', periods=len(data), freq='D')
        series = pd.Series(data, index=index)
        window_size = 3

        real_result = list(series.rolling(window_size, min_periods=1).mean())
        test_result = list(get_moving_average(series, window_size))

        self.assertEquals(real_result, test_result)


if __name__ == "__main__":
    unittest.main()