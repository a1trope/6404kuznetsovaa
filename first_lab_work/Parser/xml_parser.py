from .function_config import FunctionConfig
import xml.etree.ElementTree as ET


def parse_xml(filename: str) -> FunctionConfig:
    try:
        root = ET.parse(filename).getroot()
        parameters = (child.text for child in root)
        n0, h, nk, a, b, c = map(float, parameters)
        n0, nk = (n0, nk) if nk > n0 else (nk, n0)
        config = FunctionConfig(n0, h, nk, a, b, c)
        return config
    except (TypeError, ValueError) as e:
        print(e)
        return FunctionConfig(0.0, 0.1, 1.0, 1.0, 1.0, 1.0)