def implement_removeprefix(s, prefix):
    if s.startwith(prefix):
        return s[len(prefix): ]
    return s

#Test
print(implement_removeprefix("hello world", "hello"))