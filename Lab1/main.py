import sys
import math
import json
import parser


def test_function(x: float, a: float, b: float, c: float) -> float:
    return a - math.cos(b * x + c) ** 2


def main() -> None:
    if len(sys.argv) > 1:
        config = parser.ParserTxt().parse_text("".join(sys.argv[1:]))
    else:
        config = parser.ParserJSON().parse("config.json")

    if config is None:
        print("Can't parse parameters")
        sys.exit(-1)

    result = {}
    for x in range(config.n0, config.nk + config.h, config.h):
        result[x] = test_function(x, config.a, config.b, config.c)

    with open("result.json", "w") as f:
        json.dump(result, f)


if __name__ == "__main__":
    main()