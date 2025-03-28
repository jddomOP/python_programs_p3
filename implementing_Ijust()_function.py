def implement_ljust(s, width):
    return s + ''* (width - len(s)) if len(s) < width else s

