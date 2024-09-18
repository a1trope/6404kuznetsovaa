from dataclasses import dataclass
import json


@dataclass(frozen=True)
class FunctionConfig:
    n0: float
    h:  float
    nk: float
    a:  float
    b:  float
    c:  float

    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case 'json':
                result_string = "{\n"
                for f_name, f_val in self.__dict__.items():
                    result_string += f"\t{f_name}: {f_val}"
                    if f_name != "c":
                        result_string += ","
                    result_string += "\n"
                result_string += "}"
                return result_string
            case 'xml':
                result_string = "<config>\n"
                for f_name, f_val in self.__dict__.items():
                    result_string += f"\t<{f_name}>{f_val}</{f_name}>\n"
                result_string += "</config>"
                return result_string
            case 'txt':
                return ', '.join((f'{f_val}' for f_val in self.__dict__.values()))
            case 'csv':
                return ', '.join((f'{f_val}' for f_val in self.__dict__.values()))
            case _:
                return ', '.join((f'{f_name}: {f_val}' for f_name, f_val in self.__dict__.items()))

    def __str__(self) -> str:
        return f"{self:txt}"

    def file_output(self, filename: str, format_spec: str) -> None:
        with open(filename, "w") as f:
            match format_spec:
                case 'json':
                    f.write(f"{self:json}")
                case 'xml':
                    f.write(f"{self:xml}")
                case 'txt':
                    f.write(f"{self:txt}")
                case 'csv':
                    f.write(f"{self:csv}")
                case _:
                    f.write(f"{self:txt}")
