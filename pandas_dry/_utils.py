def flatten_strings(names, sep):
    if not isinstance(names, str):
        names = map(str, names)
    return sep.join(names)
