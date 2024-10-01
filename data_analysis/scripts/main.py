from datetime import datetime
from data_analysis.analyser.data_miner import get_temperature_series
from data_analysis.analyser.data_analyser import get_moving_average, get_autocorrelation


def main():
    start = datetime(2024, 9, 1)
    end = datetime(2024, 9, 30)

    lat, lon, alt = 53.12, 50.06, 100  # Самара городок
    df = get_temperature_series(lat, lon, alt, start, end)

    print(get_autocorrelation(df))
    print(get_moving_average(df, 1))



if __name__ == "__main__":
    main()
