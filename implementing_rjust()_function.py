def implement_rjust(s, width):
    return ' ' * (width - len(s)) + s if len(s) < width else s

#Sample usage
print(implement_rjust("Hello", 10))
