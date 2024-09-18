from dataclasses import dataclass


@dataclass(frozen=True)
class FunctionConfig:
    n0: float
    h: float
    nk: float
    a: float
    b: float
    c: float

    def __format__(self, format_spec: str) -> str:
        # print(f"{f_config:csv}")
        match format_spec:
            case 'json': return ''
            case 'html': return ''
            case 'txt': return ''
            case 'csv': return ''
            case _:
                return ', '.join(f'{f_name}: {f_val}' for f_name, f_val in zip(self.__dict__.values()))
