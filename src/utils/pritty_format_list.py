import re


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


def parse_pretty_formatted_list(text):

    tokens = re.findall(r"\[|\]|'[^']*'|\"[^\"]*\"|\S+", text)
    index = 0

    def parse():
        nonlocal index
        result = []

        while index < len(tokens):
            token = tokens[index]
            if token == "[":
                index += 1
                result.append(parse())
            elif token == "]":
                index += 1
                return result
            elif token.startswith("'") or token.startswith('"'):
                result.append(eval(token))  # sicheres Unquoting
                index += 1
            else:
                # Not expected in your case, but fallback for non-quoted tokens
                result.append(token)
                index += 1

        return result

    return parse()
