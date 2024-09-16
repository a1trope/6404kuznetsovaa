import sys
import math
import json
import parser


# def f(x, a, b, c):
#     return a - math.cos(b * x + c) ** 2
#
#
# config = parser.ParserJSON().parse("config.json")
#
# result = {}
# for x in range(config.n0, config.nk + config.h, config.h):
#     result[x] = f(x, config.a, config.b, config.c)
#
#
# with open("results.json", "w") as f:
#     json.dump(result, f)

print(sys.argv[1:])