def implement_ljust(s, width):
    return s + ''* (width - len(s)) if len(s) < width else s

print(f"{implement_ljust('Hello', 10)}")

