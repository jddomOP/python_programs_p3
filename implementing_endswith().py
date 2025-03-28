def implement_endswith(s , suffix):
    return s[-len(suffix):] == suffix if len(suffix) <= len(s) else False

print(implement_endswith("HelloWorld", "World"))