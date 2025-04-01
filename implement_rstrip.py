def implement_rstrip(s):
    while s and s[-1] == ' ':
        s = s[:-1]
    return s

test_string = '     Hello World     '
print(implement_rstrip(test_string))
