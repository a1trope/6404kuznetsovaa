import Parser
import math


def test_function(x: float, a: float, b: float, c: float) -> float:
    return a - math.cos(b * x + c) ** 2


def main() -> None:
    config = Parser.parse_json("config.json")
    # config = Parser.parse_csv("config.csv")
    # config = Parser.parse_xml("config.xml")
    # config = Parser.command_line_parser()

    # print(f"{config:json}")
    # print(f"{config:xml}")

    config.file_output("result.txt", "json")


if __name__ == "__main__":
    main()
