def implement_startswith(s, prefix):
    return s[:len(prefix)] == prefix

print(implement_startswith("hello world", "hello"))
