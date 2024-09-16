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
    def parse(self, filename: str) -> Config | None:
        try:
            with open(filename, "r") as f:
                json_file = json.loads(f.read())
                config = Config(**json_file)
                if config.n0 > config.nk:
                    return None
                return config
        except (FileNotFoundError, json.decoder.JSONDecodeError, TypeError) as e:
            print(e)
            return None


class ParserTxt:
    def parse_text(self, text: str) -> Config | None:
        try:
            config = Config(*map(int, text.split()))
            if config.n0 > config.nk:
                return None
            return config
        except (TypeError, ValueError) as e:
            print(e)
            return None


if __name__ == "__main__":
    parser = ParserJSON()
    print(ParserJSON().parse("config.json"))
    print(ParserTxt().parse_text("0 1 10 1 1 1"))
