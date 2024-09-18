from .function_config import FunctionConfig
import csv


def parse_csv(filename: str) -> FunctionConfig:
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f, delimiter=',')
            lines = [line for line in reader]
            n0, h, nk, a, b, c = map(float, lines[0])
            n0, nk = (n0, nk) if nk > n0 else (nk, n0)
            config = FunctionConfig(n0, h, nk, a, b, c)
            return config
    except (TypeError, ValueError, FileNotFoundError) as e:
        print(e)
        return FunctionConfig(0.0, 0.1, 1.0, 1.0, 1.0, 1.0)
