from .function_config import FunctionConfig


def parse_text(text: str) -> FunctionConfig:
    try:
        n0, h, nk, a, b, c = map(float, text.split())
        n0, nk = (n0, nk) if nk > n0 else (nk, n0)
        return FunctionConfig(n0, h, nk, a, b, c)
    except (TypeError, ValueError) as e:
        print(e)
        return FunctionConfig(0.0, 0.1, 1.0, 1.0, 1.0, 1.0)