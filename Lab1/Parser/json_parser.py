from .function_config import FunctionConfig
import json


def parse_json(filename: str) -> FunctionConfig:
    try:
        with open(filename, "r") as f:
            json_file = json.loads(f.read())
            n0, h, nk, a, b, c = json_file.values()
            n0, nk = (n0, nk) if nk > n0 else (nk, n0)
            config = FunctionConfig(n0, h, nk, a, b, c)
            return config
    except (TypeError, ValueError) as e:
        print(e)
        return FunctionConfig(0.0, 0.1, 1.0, 1.0, 1.0, 1.0)
