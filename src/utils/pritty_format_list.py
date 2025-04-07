def pretty_format_list(data, indent=0):
    spacing = "  " * indent
    result = ""
    if isinstance(data, list):
        result += f"{spacing}[\n"
        for item in data:
            result += pretty_format_list(item, indent + 1) + "\n"
        result += f"{spacing}]"
    else:
        result += f"{spacing}{repr(data)}"
    return result
