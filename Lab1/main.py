import Parser
import math


def test_function(x: float, a: float, b: float, c: float) -> float:
    return a - math.cos(b * x + c) ** 2


def get_values(config: Parser.FunctionConfig) -> dict:
    values = {}
    x = config.n0
    while x < config.nk:
        values[x] = test_function(x, config.a, config.b, config.c)
        x += config.h
    return values


def main() -> None:
    config = Parser.parse_json("config.json")
    # config = Parser.parse_csv("config.csv")
    # config = Parser.parse_xml("config.xml")
    # config = Parser.command_line_parser()

    # print(f"{config:json}")
    # print(f"{config:xml}")

    values = get_values(config)
    file_format = "xml"
    with open(f"Lab1/output.{file_format}", "w") as f:
        f.write(Parser.serialize_values(values, file_format=file_format))


if __name__ == "__main__":
    main()
