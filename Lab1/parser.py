import json
from dataclasses import dataclass


@dataclass
class Config:
    n0: int
    h: int
    nk: int
    a: int
    b: int
    c: int


class ParserJSON:
    def __init__(self):
        pass

    def parse(self, filename) -> Config:
        with open(filename, "r") as f:
            json_file = json.loads(f.read())
            return Config(**json_file)


if __name__ == "__main__":
    parser = ParserJSON()
    print(parser.parse("config.json"))
