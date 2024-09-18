from .function_config import FunctionConfig
import argparse


def command_line_parser() -> FunctionConfig:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n0", type=float)
    parser.add_argument("--h", type=float)
    parser.add_argument("--nk", type=float)

    parser.add_argument("--a", type=float)
    parser.add_argument("--b", type=float)
    parser.add_argument("--c", type=float)
    return FunctionConfig(*tuple(v for v in parser.parse_args().__dict__.values()))
# print(argv)

