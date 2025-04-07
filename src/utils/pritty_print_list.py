def pretty_print_list(data, indent=0):
    spacing = "  " * indent
    if isinstance(data, list):
        print(f"{spacing}[")
        for item in data:
            pretty_print_list(item, indent + 1)
        print(f"{spacing}]")
    else:
        print(f"{spacing}{repr(data)}")
    return data
