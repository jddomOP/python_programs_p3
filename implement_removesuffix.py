def implement_removesuffix(s, suffix):
    if s.endswith(suffix):
        return s[:-len(suffix)]
    return s

print(implement_removesuffix("Hello world", "world"))