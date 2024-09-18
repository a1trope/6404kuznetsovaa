def serialize_values(values: dict, file_format: str = "json"):
    match file_format:
        case 'json':
            result_string = "{\n" + ",\n".join((f'\t{k}: {v}' for k, v in values.items())) + "\n}"
            return result_string
        case 'xml':
            result_string = "<result>\n"
            for f_name, f_val in values.items():
                result_string += f"\t<{f_name}>{f_val}</{f_name}>\n"
            result_string += "</result>"
            return result_string

        case 'txt':
            return ', '.join((f'{f_val}' for f_val in values.values()))

        case 'csv':
            return ', '.join((f'{f_val}' for f_val in values.values()))

        case _:
            return ', '.join((f'{f_name}: {f_val}' for f_name, f_val in values.items()))
